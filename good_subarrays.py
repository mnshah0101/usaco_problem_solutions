import sys
from collections import defaultdict


test_cases = int(input())


def solve():
    l = int(input())
    arr = [int(x) for x in list(input())]

    prefix = [0] * l
    total = 0
    tracker = defaultdict(int)

    # Initial condition
    tracker[0] = 1  # This accounts for cases where prefix sum itself is the target

    for i in range(l):
        prefix[i] = arr[i] + (prefix[i-1] if i > 0 else 0)
        # i + 1 because of 1-based indexing assumption
        look_for = prefix[i] - (i + 1)

        # Count how many times this value has appeared
        total += tracker[look_for]

        tracker[look_for] += 1  # Update count for this prefix sum difference

    print(total)


for _ in range(test_cases):
    solve()
