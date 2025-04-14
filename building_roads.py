import sys
from itertools import combinations
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')
from collections import defaultdict


n, m = [int(x) for x in input().split()]

roads = defaultdict(set)

for _ in range(m):
    a,b = [int(x) for x in input().split()]
    roads[a].add(b)
    roads[b].add(a)

seen = set()


def dfs(i):
    
    if i not in seen:
        seen.add(i)
        for n in roads[i]:
            if n not in seen:
                dfs(n)
    
islands = 0

representatives = []

for i in range(1, n+1):
    if i in seen:
        continue
    islands += 1
    representatives.append(i)
    dfs(i)


print(islands - 1)
new_roads = []
for i in range(len(representatives)):
    if i:
        new_roads.append((representatives[i-1], representatives[i]))

print(new_roads)

    



