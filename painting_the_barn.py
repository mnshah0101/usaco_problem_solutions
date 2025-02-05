import sys

sys.stdin = open('paintbarn.in', 'r')
sys.stdout = open('paintbarn.out', 'w')


n, k = [int(x) for x in input().split()]

arr = [[0 for _ in range(1000)] for _ in range(1000)]

for i in range(n):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    arr[x1][y1] += 1
    arr[x2][y2] += 1
    arr[x1][y2] -= 1
    arr[x2][y1] -= 1


total = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i:
            arr[i][j] += arr[i-1][j]

        if j:
            arr[i][j] += arr[i][j-1]

        if i and j:
            arr[i][j] -= arr[i-1][j-1]

        if arr[i][j] == k:
            total += 1

print(total)

        
    

    