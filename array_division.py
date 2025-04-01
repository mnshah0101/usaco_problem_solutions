import sys
from bisect import bisect_left, bisect_right

# Use file redirection.
sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

n, k = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

def can_divide(max_sum):
    curr_sum = 0
    total_buckets = 1
    for num in arr:
        if curr_sum + num > max_sum:
            curr_sum = 0
            total_buckets += 1
            
        if total_buckets > k:
            return False
        
        curr_sum += num

    return total_buckets <= k


low = max(arr)
high = sum(arr)

while low < high:
    mid = (low+high) // 2
    if can_divide(mid):
        high = mid
    else:
        low = mid + 1

print(low)



