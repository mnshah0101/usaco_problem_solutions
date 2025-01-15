


n = int(input())

arr = [int(x) for x in input().split()]

arr.sort(reverse=True)


max_profit = 0
max_price = 0


for i, cow in enumerate(arr):
    profit = (i+1) * cow
    if profit >= max_profit:
        max_profit = profit
        max_price = cow

print(f'{max_profit} {max_price}')
