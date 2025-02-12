import sys

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')


n, k, q = [int(x) for x in input().split()]

recipes = []


for _ in range(n):
    recipes.append([int(x) for x in input().split()])

questions = []
for _ in range(q):
    questions.append([int(x) for x in input().split()])

arr = [0] * 200001
tracker = [0] * 200001

print(recipes)

for a, b in recipes:
    arr[a] += 1
    arr[b+1] -= 1

for i in range(len(arr)):
    if i:
        arr[i] += arr[i-1]
    if arr[i] == k:
        tracker[i] = 1
    if i:
        tracker[i] += tracker[i-1]




other_arr = [0] * 200001
for a, b in questions:
    print(tracker[b] - tracker[a-1])





