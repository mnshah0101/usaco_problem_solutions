with open("test.in") as read:
	n, m, r = [int(i) for i in read.readline().split()]

	milk_amt = [int(read.readline()) for _ in range(n)]
	shops = [[int(i) for i in read.readline().split()] for _ in range(m)]
	rent = [int(read.readline()) for _ in range(r)]

# sort cows by milk production in descending order
milk_amt.sort(reverse=True)
# sort shops by selling price in descending order
shops.sort(reverse=True, key=lambda s: s[1])
# sort rent in descending order
rent.sort(reverse=True)

shop_at = 0  # the index of the shop which we've bought up to
rent_at = 0  # the index of the farmer we've rented up to
cow_at = 0
max_money = 0
while cow_at < n:
	amt = milk_amt[cow_at]
	sold_money = 0  # how much we can make from selling the milk
	curr_shop = shop_at
	last = 0

	# calculate how much money this cow can make if we sell its milk
	while curr_shop < m:
		sold = min(amt, shops[curr_shop][0])
		sold_money += shops[curr_shop][1] * sold
		amt -= sold

		if amt == 0:
			last = sold
			break
		else:
			curr_shop += 1

	# should we rent or sell this cow?
	if rent_at >= r or sold_money > rent[rent_at]:
		max_money += sold_money
		shop_at = curr_shop
		if shop_at < m:
			shops[shop_at][0] -= last
		cow_at += 1
	else:
		max_money += rent[rent_at]
	
		n -= 1
		rent_at += 1

print(max_money, file=open("test.out", "w"))
