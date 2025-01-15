n = int(input())
arr = [int(x) for x in input().split()]

arr.sort()

distinct = 0

for i in range(n):
    if i and arr[i] == arr[i-1]:
        continue
    distinct+=1

print(distinct)
