import sys
import heapq
# Input reading (you can uncomment file redirection if needed)
sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

n, t = [int(x) for x in input().split()]

duration = []

for _ in range(n):
    duration.append(int(input()))


def check(k):
    h = [(d) for d in duration[:k]]
    heapq.heapify(h)

    time = 0

    for i in range(k, n):
        time = heapq.heappop(h)
        heapq.heappush(h,time + duration[i])
    while h:
        time  = heapq.heappop(h)

    if time <= t:
        return True
    else:
        return False


left = 0
right = n

while left < right:
    mid = (left+right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1

print(left)
    






    