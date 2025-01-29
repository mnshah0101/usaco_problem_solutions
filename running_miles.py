for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	pref = [0] * n
	suff = [0] * n

	for i in range(n):
		pref[i] = a[i] + i
		suff[i] = a[i] - i

	for i in range(1, n):
		pref[i] = max(pref[i], pref[i - 1])
	for i in range(n - 2, -1, -1):
		suff[i] = max(suff[i], suff[i + 1])

	ans = 0
	for i in range(1, n - 1):
		ans = max(ans, pref[i - 1] + suff[i + 1] + a[i])

	print(ans)
