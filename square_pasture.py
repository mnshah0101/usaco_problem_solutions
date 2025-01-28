import sys

sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")

a1, b1, c1, d1 = [int(x) for x in input().split()]

a2 , b2, c2 ,d2 = [int(x) for x in input().split()]


max_x = max(a1,c1,a2,c2)
max_y = max(b1,d1,b2,d2)

min_x = min(a1, c1, a2, c2)
min_y = min(b1, d1, b2, d2)


print(max((max_x-min_x), (max_y - min_y))**2)


