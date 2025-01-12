k, n, w = [int(x) for x in input().split()]


total_cost = 0
for i in range(1, w+1):
    total_cost += i*k

print(max(0,total_cost - n))
