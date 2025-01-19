import sys
from copy import deepcopy
from collections import defaultdict
sys.stdin = open('planting.in', 'r')
sys.stdout = open('planting.out', 'w')

adj = defaultdict(list)


result = 0
n = int(input())
for i in range(n-1):
    x, y = [int(x) for x in input().split()]
    adj[x].append(y)
    adj[y].append(x)



for key, ns in adj.items():
    result = max(result, len(ns))

print(result+1)
