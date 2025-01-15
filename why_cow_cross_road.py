import sys
sys.stdin = open('cowqueue.in', 'r')
sys.stdout = open('cowqueue.out', 'w')



n  = int(input())



cows = []

for i in range(n):
    cows.append([int(x) for x in input().split()])

cows.sort()


curr = 0

for start, l in cows:
    curr = max(curr+l, start + l)

print(curr)
