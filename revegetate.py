import sys
from collections import defaultdict

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')


adj = defaultdict(list)

n, b = [int(x) for x in input().split()]

for _ in range(b):
    x,y = [int(x) for x in input().split()]

    adj[x].append(y)
    adj[y].append(x)


colors = [0] * n



for node in range(1,n+1):
    index = node - 1

    neighbors = adj[node]

    avaiable = set([1,2,3,4])

    for neighbor in neighbors:
        if colors[neighbor - 1] in avaiable:
            avaiable.remove(colors[neighbor - 1])
        
        colors[index] = min(avaiable)


print(''.join([str(x) for x in colors]))






