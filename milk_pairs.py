import sys

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

n = int(input())

arr = []

m = 0

for i in range(n):
    arr.append([int(x) for x in input().split(" ")])
    m += arr[-1][0]

arr.sort(key = lambda x:(x[1],x[0]))

max_dist = 0


left = 0
right = n-1

for i in range(m):
    if arr[left][0] == 0:
        left += 1
    if arr[right][0] == 0:
        right -=1
    
    max_dist = max(max_dist, arr[left][1] + arr[right][1])

    arr[left][0] -= 1
    arr[right][0] -= 1 




print(max_dist)



