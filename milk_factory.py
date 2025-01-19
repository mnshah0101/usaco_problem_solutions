import sys
from collections import defaultdict

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')




n = int(input())

reversed_adj = defaultdict(list)

visited = []

for _ in range(n-1):
    x, y  = [int(x) for x in input().split()]
    reversed_adj[y].append(x)

#lets run dfs from every node and make sure the visited_set has all the stuff


def dfs(node):
    visited.add(node)
    neighbors = reversed_adj[node]

    for neighbor in neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor)



ans = -1
for node in range(1,n+1):
    visited = set()
    dfs(node)
    if len(visited) == n:
        ans = node
    visited = set()


print(ans)



