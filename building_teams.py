from collections import defaultdict
import sys
from itertools import combinations
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')


n, m = [int(x) for x in input().split()]

friendships = defaultdict(set)

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    friendships[a].add(b)
    friendships[b].add(a)

seen = set()

color_arr = [None] * (n+1)




def dfs(i, color):
    if i not in seen:
        seen.add(i)
        color_arr[i] = color
        for friend in friendships[i]:
            if color_arr[friend] and color_arr[friend]:
                print("IMPOSSIBLE")
                sys.exit()
            if friend not in seen:
                dfs(friend, (color + 1) % 2)


for i in range(n):
    if i not in seen:
        dfs(i, 0)


print(color_arr[1:])



