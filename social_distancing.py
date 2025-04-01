import sys
# Input reading (you can uncomment file redirection if needed)
sys.stdin = open("socdist.in", "r")
sys.stdout = open("socdist.out", "w")

n, m = [int(x) for x in input().split()]
intervals = [ [int(x) for x in input().split()] for _ in range(m) ]
intervals.sort()

def check(d):
    count = 1  # first cow placed at the very first grass position
    last_pos = intervals[0][0]
    
    for l, r in intervals:
        # While we can place a cow in the current interval
        while max(last_pos + d, l) <= r:
            # Place the next cow at the maximum of (last_pos + d) and the start of the interval
            last_pos = max(last_pos + d, l)
            count += 1
            if count >= n:
                return True
    return False

left = 1
right = intervals[-1][1] - intervals[0][0]
ans = 0

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
