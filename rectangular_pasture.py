import sys

# Sample Input:
# 4
# 0 2
# 1 0
# 2 3
# 3 5

n = int(input())

cows = []
x_arr = []
# We don't really need y_arr for this solution, so it's omitted.

for i in range(n):
    x, y = map(int, input().split())
    cows.append((x, y))
    x_arr.append((x, i))  # Store (x-coordinate, original index)

# Sort cows by x-coordinate
x_arr.sort()

ans = 0

# Loop over all pairs of x boundaries (using indices in the sorted order)
for left in range(n):
    for right in range(left, n):
        # Get the original indices for the left and right boundary cows
        left_idx = x_arr[left][1]
        right_idx = x_arr[right][1]

        left_x = x_arr[left][0]
        right_x = x_arr[right][0]
        # Get the y-coordinates for the boundaries correctly
        top_y = max(cows[left_idx][1], cows[right_idx][1])
        bottom_y = min(cows[left_idx][1], cows[right_idx][1])

        top = 0
        bottom = 0

        # Look at every cow between the left and right boundaries in the sorted order
        for j in range(left, right + 1):
            cow_index = x_arr[j][1]   # Original index of the cow
            cow_x = x_arr[j][0]         # x-coordinate (already sorted)
            cow_y = cows[cow_index][1]  # y-coordinate from the original list

            # Only consider cows strictly inside the x-boundaries
            if cow_x > left_x and cow_x < right_x:
                if cow_y > top_y:
                    top += 1
                if cow_y < bottom_y:
                    bottom += 1

        ans += (top + 1) * (bottom + 1)

# The final answer adds one more for the empty subset.
print(ans + 1)
