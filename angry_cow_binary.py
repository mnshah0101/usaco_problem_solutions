import sys
from bisect import bisect_left, bisect_right

# Use file redirection.
sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out", "w")

# Increase recursion limit (worst-case chain depth can be high).
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline().strip())
bales = [int(sys.stdin.readline().strip()) for _ in range(n)]

# Double all coordinates to avoid dealing with floats.
bales = [x * 2 for x in bales]
bales.sort()

MAX_POS = 10**9

def push(pos, idx, r, direction):
    """
    Recursively simulate the chain reaction.
    
    pos: current explosion position (doubled)
    idx: index of the hay bale reached at this explosion
    r: current blast radius (doubled; note that each explosion reduces r by 2)
    direction: 0 for rightward propagation, 1 for leftward propagation.
    
    Returns True if the chain reaction reaches the extreme bale in that direction.
    """
    if r < 0:
        return False

    if direction == 0:  # Propagate to the right.
        # If current explosion reaches the rightmost bale, we are done.
        if pos + r >= bales[-1]:
            return True
        new_idx = idx
        # Find the farthest bale within reach.
        while new_idx < n and pos + r >= bales[new_idx]:
            new_idx += 1
        if new_idx == idx:  # no progression
            return False
        # Recurse from the last bale that was reached.
        return push(bales[new_idx - 1], new_idx, r - 2, direction)
    else:  # Propagate to the left.
        if pos - r <= bales[0]:
            return True
        new_idx = idx
        # Move left: decrement new_idx while the bale is within reach.
        while new_idx >= 0 and pos - r <= bales[new_idx]:
            new_idx -= 1
        if new_idx == idx:  # no progression
            return False
        return push(bales[new_idx + 1], new_idx, r - 2, direction)

# Outer binary search over the possible (doubled) initial power.
lo = 0
hi = MAX_POS * 2  # maximum possible doubled radius

while lo < hi:
    power = lo + (hi - lo) // 2
    
    # Inner binary search for the best landing position for the cow (to propagate leftward).
    pos_lo = 0
    pos_hi = MAX_POS * 2
    while pos_lo < pos_hi:
        pos = pos_lo + (pos_hi - pos_lo + 1) // 2
        close = bisect_left(bales, pos)
        # Check if starting an explosion at 'pos' can push left (direction = 1).
        if close < n and push(pos, close, power, 1):
            pos_lo = pos
        else:
            pos_hi = pos - 1
    # Now check if from the best leftward landing we can push right (direction = 0). basically looking for highest point that leftward is covered.
    close = bisect_right(bales, pos_lo)
    if push(pos_lo, close, power, 0):
        hi = power
    else:
        lo = power + 1

# The computed 'lo' is our answer in doubled units; scale back by dividing by 2.
result = lo / 2.0
print(f"{result:.1f}")
