import sys
from bisect import bisect

#sys.stdin = open("test.in", "r")
#sys.stdout = open("test.out", "w")



g, n = [int(x) for x in input().split()]

grazers = []
for _ in range(g):
    x,y, t = [int(x) for x in input().split()]
    grazers.append((t,x,y))


def reachable(a, b):
    return (a[1]-b[1])**2 + (a[2]-b[2])**2 <= (a[0]-b[0])**2


grazers.sort()
tot = 0
for i in range(n):
    #alibi
    x,y, t = [int(x) for x in input().split()]
    pos = bisect(grazers, (t,x,y))

    innocent = False
    for ny in (pos-1, pos):
        if 0 <= ny < g:
            innocent |= not reachable(grazers[ny], (t,x,y))
    

    tot += innocent

print(tot)



    