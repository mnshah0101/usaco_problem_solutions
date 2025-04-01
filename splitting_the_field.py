import sys

sys.stdin = open('split.in', 'r')
sys.stdout = open('split.out', 'w')

n = int(input())
cows = []
for _ in range(n):
    x, y = map(int, input().split())
    cows.append((x, y))

# Sort cows by x-coordinate and y-coordinate separately.
cows_x = sorted(cows)
cows_y = sorted(cows, key=lambda cow: cow[1])

# Compute area of one large rectangle that encloses all cows.
one_area = (cows_x[-1][0] - cows_x[0][0]) * (cows_y[-1][1] - cows_y[0][1])


def search(cows, dim=0):
    """
    Given cows sorted by the coordinate specified by 'dim' (0 for x, 1 for y),
    compute the minimal total area when splitting the cows into two groups
    with a separation between cows[i] and cows[i+1] (i.e. cows[i][dim] < cows[i+1][dim]).
    
    Each group’s area is determined by its bounding rectangle.
    """
    n = len(cows)
    # prefix[i] will store (min_x, max_x, min_y, max_y) for cows[0..i]
    prefix = [None] * n
    suffix = [None] * n  # suffix[i] for cows[i..n-1]

    # Initialize prefix for the first cow.
    prefix[0] = (cows[0][0], cows[0][0], cows[0][1], cows[0][1])
    for i in range(1, n):
        x, y = cows[i]
        min_x, max_x, min_y, max_y = prefix[i-1]
        prefix[i] = (min(min_x, x), max(max_x, x),
                     min(min_y, y), max(max_y, y))

    suffix[-1] = (cows[-1][0], cows[-1][0], cows[-1][1], cows[-1][1])
    for i in range(n-2, -1, -1):
        x, y = cows[i]
        min_x, max_x, min_y, max_y = suffix[i+1]
        suffix[i] = (min(min_x, x), max(max_x, x),
                     min(min_y, y), max(max_y, y))

    best = float('inf')
    for i in range(n-1):
        if cows[i][dim] < cows[i+1][dim]:
            lmin_x, lmax_x, lmin_y, lmax_y = prefix[i]
            rmin_x, rmax_x, rmin_y, rmax_y = suffix[i+1]
            area_left = (lmax_x - lmin_x) * (lmax_y - lmin_y)
            area_right = (rmax_x - rmin_x) * (rmax_y - rmin_y)
            best = min(best, area_left + area_right)
    return best


best_vertical = search(cows_x, dim=0)
best_horizontal = search(cows_y, dim=1)
best_split_area = min(best_vertical, best_horizontal)

if best_split_area == float('inf'):
    best_split_area = one_area

print(one_area - best_split_area)
