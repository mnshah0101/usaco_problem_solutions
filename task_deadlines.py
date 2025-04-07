import sys

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")


n = int(input())

arr = []

for _ in range(n):
    arr.append([int(x) for x in input().split()])

arr.sort()

total = 0
time = 0
for i in range(n):
    time += arr[i][0]
    total += (arr[i][1] - time)

print(total)
