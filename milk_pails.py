import sys
sys.stdin = open("pails.in", 'r')
sys.stdout = open("pails.out", 'w')

x, y, m = [int(x) for x in input().split()]

total = 0

max_x = m//x
max_y = m//y



for i in range(max_x):
    y_part = ((m-i*x)//y) * y
    total = max(total, i*x + y_part)

for i in range(max_y):
    x_part = ((m-i*y)//x) * x
    total = max(total, i*y + x_part)

print(total)
