#capacity then amount
import sys

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")
import heapq
from collections import deque



def solve():

    n = int(input())


    intervals = []

    right = 0

    for _ in range(n):
        intervals.append([int(x) for x in input().split()])
        right = max(right, intervals[-1][-1])




    intervals = deque(intervals)
    q = []

    for i in range(1, right + 2):
        if intervals and i >= intervals[0][0]:
            interval = intervals.popleft()
            heapq.heappush(q, (interval[1], interval[0]))
        
        if q and i <= q[0][0] and i>= q[0][1] :
            heapq.heappop(q)

        if q and i > q[0][0] and i < q[0][1]:
            break


    if q:
        print("No")
    else:
        print("Yes")


        
        
T = int(input())

for i in range(T):

    solve()
