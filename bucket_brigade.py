import sys

sys.stdin = open("buckets.in", "r")
sys.stdout = open("buckets.out", "w")

matrix = [input().strip() for _ in range(10)]

B = L = R = None
for r in range(10):
    for c in range(10):
        if matrix[r][c] == 'B':
            B = (r, c)
        elif matrix[r][c] == 'L':
            L = (r, c)
        elif matrix[r][c] == 'R':
            R = (r, c)

# Manhattan distance between B and L
base_dist = abs(B[0] - L[0]) + abs(B[1] - L[1]) - 1

# Check same row
if B[0] == L[0] == R[0]:
    # See if R is strictly between them horizontally
    if min(B[1], L[1]) < R[1] < max(B[1], L[1]):
        base_dist += 2

# Check same column
elif B[1] == L[1] == R[1]:
    # See if R is strictly between them vertically
    if min(B[0], L[0]) < R[0] < max(B[0], L[0]):
        base_dist += 2

print(base_dist)
