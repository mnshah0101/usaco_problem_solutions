import sys

sys.stdin = open("lazy.in", "r")

n, k = map(int, input().split())
# the side length needed to accomodate the 45 degree rotation
new_n = 2 * n - 1
field = [[-1] * new_n for _ in range(new_n)]  # -1's indicate invalid locations

# read input and store it rotated by 45 degrees
for i in range(n):
	for j, x in enumerate(map(int, input().split())):
		field[i + j][n - i + j - 1] = x

prefix = [[0] * (new_n + 1) for _ in range(new_n + 1)]
for i in range(new_n):
	for j in range(new_n):
		val = max(field[i][j], 0)  # prevent including -1's in the prefix sum
		prefix[i + 1][j + 1] = val + prefix[i + 1][j] + \
			prefix[i][j + 1] - prefix[i][j]

most_grass = 0
for i in range(k, new_n - k):
	for j in range(k, new_n - k):
		if field[i][j] == -1:
			continue  # don't start at invalid locations
		most_grass = max(
			most_grass,
			prefix[i + k + 1][j + k + 1]
			- prefix[i + k + 1][j - k]
			- prefix[i - k][j + k + 1]
			+ prefix[i - k][j - k],
		)

if k >= n:
	# check if Bessie can reach everything
	most_grass = prefix[new_n][new_n]

sys.stdout = open("lazy.out", "w")
print(most_grass)
