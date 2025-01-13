import sys
from itertools import combinations
sys.stdin = open('cownomics.in', 'r')
sys.stdout = open('cownomics.out', 'w')


s, p = [int(x) for x in input().split()]

spotty = []
plain = []

for i in range(s):
    spotty.append(input())
for i in range(s):
    plain.append(input())


arr = list(range(p))

combs = combinations(arr, 3)


total = 0

for x, y, z in combs:
    spotty_set = set()
    plain_set = set()

    for cow in spotty:
        spotty_set.add((cow[x], cow[y], cow[z]))
    for cow in plain:
        plain_set.add((cow[x], cow[y], cow[z]))

    if len(plain_set.intersection(spotty_set)) == 0:
        total += 1

print(total)


