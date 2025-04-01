import sys

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

n, t = [int(x) for x in input().split(' ')]
arr = [int(x) for x in input().split(' ')]


left = 0

max_books = 0

curr_t = t

for right in range(len(arr)):
    curr_t -= arr[right]
    while curr_t < 0 and left < len(arr):
        curr_t += arr[left]
        left += 1
    max_books = max(max_books, right - left + 1)

print(max_books)
    




