import sys

# Redirect input/output (make sure that test.in exists)
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')

# Read input dimensions and query count
n, m, q = map(int, input().split())

# Read the grid; assume each line contains a string of digits with no spaces
grid = []
for _ in range(n):
    # Remove any stray whitespace/newlines with .strip()
    grid.append([int(x) for x in list(input().strip())])
print(grid)  # Debug print (you might want to remove it later)

# Read the queries (adjusting the indices to be 0-based)
queries = []
for _ in range(q):
    # Subtract 1 from each coordinate to convert from 1-based to 0-based indexing
    queries.append([int(x) - 1 for x in input().split()])

# Build the prefix grid
prefix = [[0 for _ in range(m)] for _ in range(n)]

# It is usually best to initialize the first row and first column
prefix[0][0] = grid[0][0]
for j in range(1, m):
    prefix[0][j] = prefix[0][j - 1] + grid[0][j]
for i in range(1, n):
    prefix[i][0] = prefix[i - 1][0] + grid[i][0]

# Now fill in the rest of the prefix grid.
# Note: The inner loop now uses range(m) instead of range(n)
for i in range(1, n):
    for j in range(1, m):
        prefix[i][j] = prefix[i - 1][j] + \
            prefix[i][j - 1] - prefix[i - 1][j - 1]
        if grid[i][j]:
            # Adjust based on the surrounding cells
            if not grid[i - 1][j] and not grid[i][j - 1]:
                prefix[i][j] += 1
            elif grid[i - 1][j] and grid[i][j - 1]:
                prefix[i][j] -= 1

# Build the horizontal and vertical arrays
horizontal = [[0 for _ in range(m)] for _ in range(n)]
vertical = [[0 for _ in range(m)] for _ in range(n)]

# It's a good idea to initialize the first row and first column if needed.
# For horizontal differences, we can initialize row 0:
for j in range(1, m):
    horizontal[0][j] = horizontal[0][j - 1] + \
        (1 if (grid[0][j] and not grid[0][j - 1]) else 0)
# Similarly, for vertical differences, initialize column 0:
for i in range(1, n):
    vertical[i][0] = vertical[i - 1][0] + \
        (1 if (grid[i][0] and not grid[i - 1][0]) else 0)

# Fill in the remaining cells for horizontal and vertical counts
for i in range(1, n):
    for j in range(1, m):
        horizontal[i][j] = horizontal[i][j - 1]
        vertical[i][j] = vertical[i - 1][j]
        if grid[i][j]:
            horizontal[i][j] += (1 if not grid[i][j - 1] else 0)
            vertical[i][j] += (1 if not grid[i - 1][j] else 0)

# Process each query
for a, b, c, d in queries:
    ans = 0
    # Compute contributions from horizontal, vertical, and prefix sums.
    ans += horizontal[a][d] - horizontal[a][b]
    ans += vertical[c][b] - vertical[a][b]
    ans += prefix[c][d] - prefix[a][d] - prefix[c][b] + prefix[a][b]
    ans += grid[a][b]

    print(ans)
