from collections import defaultdict
import sys
from itertools import combinations
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')

n = int(input())

cows = []

for i in range(n):
    cows.append([int(x) for x in input().split()])

#x,y distance

graph = defaultdict(set)


def distance(x1,y1, x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

for i in range(len(cows)):
    for j in range(i + 1, len(cows)):
        cow_1 = cows[i]
        cow_2 = cows[j]
        d = distance(cow_1[0],  cow_1[1], cow_2[0], cow_2[1])

        if d <= cow_1[-1]:
            graph[i].add(j)
        if d<= cow_2[-1]:
            graph[j].add(i)


def dfs(i, seen):
    if i not in seen:
        seen.add(i)
        for n in graph[i]:
            if n not in seen:
                dfs(n, seen)

max_cows = 1
for cow in range(n):
    seen = set()
    dfs(cow, seen)
    max_cows = max(max_cows, len(seen))

    
print(max_cows)
    



