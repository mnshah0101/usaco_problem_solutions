import sys

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')


n, m, k = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]




operations = []

for _ in range(m):
    operations.append([int(x) for x in input().split()])
queries = []
for _ in range(k):
    queries.append([int(x) for x in input().split()])


operation_freq = [0] * (m + 1)
for x, y in queries:
    x, y = x-1, y-1
    operation_freq[x] += 1
    operation_freq[y + 1] -= 1

for i in range(len(operation_freq)):
    if i:
        operation_freq[i] += operation_freq[i-1]




diff_arr = [0] * (n+1)
    
for i in range(m):
    l, r, d = operations[i]
    freq = operation_freq[i]
    diff_arr[l-1] += d * freq
    if r < n:
        diff_arr[r] -= d * freq


for i in range(n):
    if i:
        diff_arr[i] += diff_arr[i-1]

    arr[i] += diff_arr[i]
    arr[i] = str(arr[i])

print(' '.join(arr))



