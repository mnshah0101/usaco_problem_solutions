n = int(input())
weights = list(map(int, input().split()))


def recurse_apples(i: int, sum1: int, sum2: int) -> int:
	# We've added all apples- return the absolute difference
	if i == n:
		return abs(sum2 - sum1)

	return min(
		recurse_apples(i + 1, sum1 + weights[i], sum2),
		recurse_apples(i + 1, sum1, sum2 + weights[i]),
	)


# Solve the problem starting at apple 0 with both sets being empty
print(recurse_apples(0, 0, 0))
