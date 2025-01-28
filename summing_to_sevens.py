import sys
sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')

MOD = 7

n = int(input())
cows = []
for _ in range(n):
	cows.append(int(input()))

best_photo = 0
first_occ = [-1 for _ in range(MOD)]
first_occ[0] = 0

running_mod = 0
for v, c in enumerate(cows):
	running_mod = (running_mod + c) % MOD

	if first_occ[running_mod] == -1:
		first_occ[running_mod] = v + 1
	else:
		best_photo = max(best_photo, v + 1 - first_occ[running_mod])
\
print(best_photo)



