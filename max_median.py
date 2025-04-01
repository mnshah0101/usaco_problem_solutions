import sys

# Input reading (you can uncomment file redirection if needed)
sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()
med = n // 2  # index of median

def check_max(x):
    total_ops = 0
    # Ensure the median and all elements to its right reach at least x
    for i in range(med, n):
        total_ops += max(0, x - arr[i])
        if total_ops > k:
            return False
    return True

left = arr[med]
right = arr[med] + k  # maximum achievable median using all operations
while left < right:
    mid = (left + right + 1) // 2  # round up to avoid infinite loop
    if check_max(mid):
        left = mid
    else:
        right = mid - 1

print(left)
