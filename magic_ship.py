import sys

# For local testing, input and output are redirected to files.
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')

# Read input values.
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
n = int(input())
dirs = input().strip()

# Compute the net displacement of one complete cycle.
px, py = 0, 0
for ch in dirs:
    if ch == 'U':
        py += 1
    elif ch == 'D':
        py -= 1
    elif ch == 'L':
        px -= 1
    elif ch == 'R':
        px += 1

# Precompute the prefix displacements for the cycle.
# prefix[i] will hold the displacement after i days (0 <= i <= len(dirs)).
prefix = [(0, 0)]
for ch in dirs:
    last_x, last_y = prefix[-1]
    if ch == 'U':
        prefix.append((last_x, last_y + 1))
    elif ch == 'D':
        prefix.append((last_x, last_y - 1))
    elif ch == 'L':
        prefix.append((last_x - 1, last_y))
    elif ch == 'R':
        prefix.append((last_x + 1, last_y))


"""
see where wind makes you end up at end, and then see if you have enough days to get there
"""
def check(days):
    """
    Returns True if it is possible to reach (x2, y2) in 'days' days.
    
    Each day the wind adds its displacement, and the ship (or you) can also
    make an extra move of at most 1 unit per day in any direction.
    """
    # Calculate how many full cycles and remaining days.
    cycle_len = len(dirs)
    full_cycles = days // cycle_len
    remainder = days % cycle_len

    # Determine the current position after `days` days.
    cur_x = x1 + full_cycles * px + prefix[remainder][0]
    cur_y = y1 + full_cycles * py + prefix[remainder][1]

    # Calculate the Manhattan distance needed to reach destination.
    dist = abs(x2 - cur_x) + abs(y2 - cur_y)
    return dist <= days


# Binary search for the minimum number of days needed.
lo, hi = 0, 10**18
ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)
