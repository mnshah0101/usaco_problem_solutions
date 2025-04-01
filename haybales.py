import sys
from bisect import bisect_left, bisect_right

sys.stdin = open("haybales.in", "r")
sys.stdout = open("haybales.out", "w")

n, q = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]
arr.sort()

queries = []

for _ in range(q):
    queries.append([int(x) for x in input().split()])

for a,b in queries:
    left_idx = bisect_left(arr, a)
    right_idx = bisect_right(arr, b)
    print( right_idx - left_idx )




