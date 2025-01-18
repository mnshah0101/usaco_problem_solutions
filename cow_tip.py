import sys
from collections import defaultdict

sys.stdin = open("cowtip.in", "r")
sys.stdout = open("cowtip.out", "w")



n = int(input())


matrix = []
for _ in range(n):
    matrix.append(list(map(lambda x: int(x), list(input()))))


def flip(r,c):
    for i in range(r+1):
        for j in range(c+1):
            matrix[i][j] = not matrix[i][j]

flips = 0
for i in range(n-1, -1, -1):
    x, y = i,i 
    for a in range(n):
        if matrix[x-a][y] == 1:
            flip(x-a, y)
            flips += 1
        if matrix[x][y-a] == 1:
            flip(x, y-a)
            flips += 1

print(flips)


