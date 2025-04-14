from typing import Dict, List
import numpy as np
import jsonpickle



import json
from typing import Dict, List, Any
from json import JSONEncoder
import jsonpickle

Time = int
Symbol = str
Product = str
Position = int
UserId = str
ObservationValue = int


class Listing:

    def __init__(self, symbol: Symbol, product: Product, denomination: Product):
        self.symbol = symbol
        self.product = product
        self.denomination = denomination


class ConversionObservation:

    def __init__(self, bidPrice: float, askPrice: float, transportFees: float, exportTariff: float, importTariff: float, sugarPrice: float, sunlightIndex: float):
        self.bidPrice = bidPrice
        self.askPrice = askPrice
        self.transportFees = transportFees
        self.exportTariff = exportTariff
        self.importTariff = importTariff
        self.sugarPrice = sugarPrice
        self.sunlightIndex = sunlightIndex


class Observation:

    def __init__(self, plainValueObservations: Dict[Product, ObservationValue], conversionObservations: Dict[Product, ConversionObservation]) -> None:
        self.plainValueObservations = plainValueObservations
        self.conversionObservations = conversionObservations

    def __str__(self) -> str:
        return "(plainValueObservations: " + jsonpickle.encode(self.plainValueObservations) + ", conversionObservations: " + jsonpickle.encode(self.conversionObservations) + ")"


class Order:

    def __init__(self, symbol: Symbol, price: int, quantity: int) -> None:
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return "(" + self.symbol + ", " + str(self.price) + ", " + str(self.quantity) + ")"

    def __repr__(self) -> str:
        return "(" + self.symbol + ", " + str(self.price) + ", " + str(self.quantity) + ")"


class OrderDepth:

    def __init__(self):
        self.buy_orders: Dict[int, int] = {}
        self.sell_orders: Dict[int, int] = {}


class Trade:

    def __init__(self, symbol: Symbol, price: int, quantity: int, buyer: UserId = None, seller: UserId = None, timestamp: int = 0) -> None:
        self.symbol = symbol
        self.price: int = price
        self.quantity: int = quantity
        self.buyer = buyer
        self.seller = seller
        self.timestamp = timestamp

    def __str__(self) -> str:
        return "(" + self.symbol + ", " + self.buyer + " << " + self.seller + ", " + str(self.price) + ", " + str(self.quantity) + ", " + str(self.timestamp) + ")"

    def __repr__(self) -> str:
        return "(" + self.symbol + ", " + self.buyer + " << " + self.seller + ", " + str(self.price) + ", " + str(self.quantity) + ", " + str(self.timestamp) + ")"




class TradingState(object):

    def __init__(self,
                 traderData: str,
                 timestamp: Time,
                 listings: Dict[Symbol, Listing],
                 order_depths: Dict[Symbol, OrderDepth],
                 own_trades: Dict[Symbol, List[Trade]],
                 market_trades: Dict[Symbol, List[Trade]],
                 position: Dict[Product, Position],
                 observations: Observation):
        self.traderData = traderData
        self.timestamp = timestamp
        self.listings = listings
        self.order_depths = order_depths
        self.own_trades = own_trades
        self.market_trades = market_trades
        self.position = position
        self.observations = observations

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)


class ProsperityEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class Trader:
    def __init__(self):
        # Strategy parameters for each product.
        # For Rainforest Resin we use a static market-making approach.
        # For PICNIC_BASKET2 we use a naked directional strategy based on JAMS.
        self.product_params = {
            # For PICNIC_BASKET2, we now use a naked directional approach.
            "PICNIC_BASKET2": {"base_order_size": 10,
                               # Minimum magnitude of JAMS momentum to trade.
                               "signal_threshold": 5,
                               # Maximum multiplier on order size.
                               "max_scale": 2.0,
                               "inv_adj_factor": 0.2},
            # For other basket(s) we can leave them (if desired) in passive mode.
            "PICNIC_BASKET1": {"order_size": 10, "arb_threshold": 1.0, "inv_adj_factor": 0.2},
            # Underlying products (only used in passive MM)
            "KELP":          {"order_size": 0, "base_spread": 3,  "inv_adj_factor": 0.2},
            "SQUID_INK":     {"order_size": 0, "base_spread": 3,  "inv_adj_factor": 0.2},
            "DJEMBES":       {"order_size": 0, "base_spread": 1,  "inv_adj_factor": 0.2},
            "CROISSANTS":    {"order_size": 0, "base_spread": 1,  "inv_adj_factor": 0.2},
            "JAMS":          {"order_size": 0, "base_spread": 2,  "inv_adj_factor": 0.2},
            # Rainforest Resin: static.
            "RAINFOREST_RESIN": {"order_size": 5, "inv_adj_factor": 0.2}
        }
        # Position limits per product.
        self.pos_limits = {
            "RAINFOREST_RESIN": 50,
            "KELP": 50,
            "SQUID_INK": 50,
            "DJEMBES": 60,
            "CROISSANTS": 250,
            "JAMS": 350,
            "PICNIC_BASKET1": 60,
            "PICNIC_BASKET2": 100
        }
        # For the directional signal, we maintain a short history of JAMS mid-prices.
        self.jams_history: List[int] = []
        self.jams_lookback = 10  # Use a window of 10 timestamps.
        # internal_state persists between iterations.
        self.internal_state: Dict = {}

    def run(self, state: TradingState):
        result: Dict[str, List[Order]] = {}
        # Initialize results for all products we track.
        for product in self.product_params:
            result[product] = []

        # --- 1. Rainforest Resin: Static Market Making ---
        if "RAINFOREST_RESIN" in state.order_depths:
            order_depth = state.order_depths["RAINFOREST_RESIN"]
            current_inventory = state.position.get("RAINFOREST_RESIN", 0)
            inv_adj_factor = self.product_params["RAINFOREST_RESIN"].get(
                "inv_adj_factor", 0.2)
            pos_limit = self.pos_limits.get("RAINFOREST_RESIN", 50)
            available_buy = pos_limit - current_inventory
            available_sell = pos_limit + current_inventory
            order_size = self.product_params["RAINFOREST_RESIN"].get(
                "order_size", 5)
            buy_order_size = min(
                order_size, available_buy) if available_buy > 0 else 0
            sell_order_size = min(
                order_size, available_sell) if available_sell > 0 else 0
            target_bid = 9992
            target_ask = 10008
            adjusted_bid = target_bid - (current_inventory * inv_adj_factor)
            adjusted_ask = target_ask - (current_inventory * inv_adj_factor)
            if buy_order_size > 0:
                result["RAINFOREST_RESIN"].append(
                    Order("RAINFOREST_RESIN", int(round(adjusted_bid)), buy_order_size))
            if sell_order_size > 0:
                result["RAINFOREST_RESIN"].append(
                    Order("RAINFOREST_RESIN", int(round(adjusted_ask)), -sell_order_size))

        # --- 2. PICNIC_BASKET2: Naked Directional Strategy Using JAMS ---
        if "PICNIC_BASKET2" in state.order_depths and "JAMS" in state.order_depths:
            # Compute the basket's mid price.
            basket_depth = state.order_depths["PICNIC_BASKET2"]
            basket_mid = self.get_fair_value_from_depth(basket_depth)
            # Get current position and limits.
            current_inventory_basket = state.position.get("PICNIC_BASKET2", 0)
            pos_limit_basket = self.pos_limits.get("PICNIC_BASKET2", 100)
            available_buy_basket = pos_limit_basket - current_inventory_basket
            available_sell_basket = pos_limit_basket + current_inventory_basket
            base_order_size = self.product_params["PICNIC_BASKET2"].get(
                "base_order_size", 10)

            # Update JAMS history for the directional signal.
            jams_depth = state.order_depths["JAMS"]
            jams_mid = self.get_fair_value_from_depth(jams_depth)
            self.jams_history.append(jams_mid)
            if len(self.jams_history) > self.jams_lookback:
                self.jams_history.pop(0)
            jams_ma = np.mean(self.jams_history)
            # Positive if JAMS is trending upward.
            jams_momentum = jams_mid - jams_ma
            # Use the directional signal (with a threshold and scaling).
            signal_threshold = self.product_params["PICNIC_BASKET2"].get(
                "signal_threshold", 5)
            beta = 0.5  # Sensitivity coefficient (tune as needed).
            # For our bearish view, if jams_momentum is significantly positive,
            # we want to increase our short exposure; if negative, we might even go long.
            # We'll define a direction factor:
            if abs(jams_momentum) < signal_threshold:
                direction_factor = 1.0  # Signal too weak
            else:
                # If JAMS is trending upward (positive momentum), we favor shorts (multiply order size).
                direction_factor = 1 + beta * \
                    (jams_momentum / signal_threshold)
                # For a bearish trader on PICNIC_BASKET2, a positive signal increases our short order size.
            # Determine our effective order size.
            effective_order_size = int(base_order_size * direction_factor)
            # Also, ensure we do not exceed position limits.
            if effective_order_size < 1:
                effective_order_size = 0

            print(f"[DEBUG - PICNIC_BASKET2 Directional]")
            print(f"    Basket Mid: {basket_mid}")
            print(
                f"    JAMS Mid: {jams_mid}, MA: {jams_ma:.2f}, Momentum: {jams_momentum:.2f}")
            print(f"    Direction Factor: {direction_factor:.2f}")
            print(
                f"    Base Order Size: {base_order_size}, Effective Order Size: {effective_order_size}")
            # Our view: if JAMS momentum is positive, we expect basket2 to be overpriced, so we short it.
            # Conversely, if JAMS momentum is negative, we might go long.
            # For this example, we focus on being bearish, so we choose to short when momentum is positive.
            if jams_momentum > 0 and effective_order_size > 0:
                # Ensure we do not exceed sell capacity.
                sell_order_size = min(
                    effective_order_size, available_sell_basket)
                if sell_order_size > 0:
                    result["PICNIC_BASKET2"].append(
                        Order("PICNIC_BASKET2", basket_mid, -sell_order_size))
                    print(
                        f"    Placing SELL order on PICNIC_BASKET2: {sell_order_size} units at {basket_mid}")
            elif jams_momentum < 0 and effective_order_size > 0:
                # If the signal is negative (JAMS falling), we go long.
                buy_order_size = min(effective_order_size,
                                     available_buy_basket)
                if buy_order_size > 0:
                    result["PICNIC_BASKET2"].append(
                        Order("PICNIC_BASKET2", basket_mid, buy_order_size))
                    print(
                        f"    Placing BUY order on PICNIC_BASKET2: {buy_order_size} units at {basket_mid}")
            else:
                print("    No clear signal for PICNIC_BASKET2.")

        # --- 3. Other Products: Passive Market Making ---
        for product, order_depth in state.order_depths.items():
            if product in ["RAINFOREST_RESIN", "PICNIC_BASKET2"]:
                continue  # Already handled.
            # For other products (and basket1, if desired) use passive market making.
            orders = []
            params = self.product_params[product]
            order_size = params.get("order_size", 10)
            base_spread = params.get("base_spread", 5)
            inv_adj_factor = params.get("inv_adj_factor", 0.2)
            current_inventory = state.position.get(product, 0)
            pos_limit = self.pos_limits.get(product, 50)
            available_buy = pos_limit - current_inventory
            available_sell = pos_limit + current_inventory
            buy_order_size = min(
                order_size, available_buy) if available_buy > 0 else 0
            sell_order_size = min(
                order_size, available_sell) if available_sell > 0 else 0
            fair_value = self.get_fair_value_from_depth(order_depth)
            bid_quote = int(round(fair_value - base_spread - (current_inventory * inv_adj_factor)))
            ask_quote = int(round(fair_value + base_spread - (current_inventory * inv_adj_factor)))
            print(f"[DEBUG - Passive MM] Product: {product}")
            print(
                f"    Fair Value: {fair_value}, Bid: {bid_quote}, Ask: {ask_quote}")
            print(f"    Current Inventory: {current_inventory}")
            if buy_order_size > 0:
                orders.append(Order(product, bid_quote, buy_order_size))
                print(
                    f"    Placing BUY limit order: {buy_order_size} units at {bid_quote}")
            if sell_order_size > 0:
                orders.append(Order(product, ask_quote, -sell_order_size))
                print(
                    f"    Placing SELL limit order: {sell_order_size} units at {ask_quote}")
            result[product] = orders

        traderData = jsonpickle.encode(self.internal_state)
        conversions = 0
        return result, conversions, traderData

    def get_fair_value_from_depth(self, order_depth: OrderDepth) -> int:
        # Compute the weighted midpoint from the order book.
        if order_depth.buy_orders:
            buy_prices = list(order_depth.buy_orders.keys())
            buy_volumes = list(order_depth.buy_orders.values())
            bid_avg = np.average(buy_prices, weights=buy_volumes)
        else:
            bid_avg = None
        if order_depth.sell_orders:
            sell_prices = list(order_depth.sell_orders.keys())
            sell_volumes = [abs(v) for v in order_depth.sell_orders.values()]
            ask_avg = np.average(sell_prices, weights=sell_volumes)
        else:
            ask_avg = None
        if bid_avg is not None and ask_avg is not None:
            fair_value = (bid_avg + ask_avg) / 2
        elif bid_avg is not None:
            fair_value = bid_avg + 1
        elif ask_avg is not None:
            fair_value = ask_avg - 1
        else:
            fair_value = 0
        return int(round(fair_value))
