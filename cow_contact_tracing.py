import sys
from collections import defaultdict

sys.stdin = open('tracing.in', 'r')
sys.stdout = open('tracing.out', 'w')

n, t = map(int, input().split())
state = input()
initial_state = set()

contacts = []
for i in range(t):
    to_append = tuple(map(int, input().split()))
    contacts.append(to_append)

for i, c in enumerate(state):
    if c == '1':
        initial_state.add(i+1)

contacts.sort()

valid_k = []
valid_cows = set()

for pz in initial_state:  # Only try infected cows as patient zero
    for k in range(251):  # Try k values up to 250
        sick = set([pz])
        times_contacted = [0] * (n + 1)  # Track contacts per cow independently

        for time, x, y in contacts:
            # Count contacts for infected cows
            if x in sick:
                times_contacted[x] += 1
            if y in sick:
                times_contacted[y] += 1

            # Spread infection if conditions are met
            if x in sick and y not in sick and times_contacted[x] <= k:
                sick.add(y)
            if y in sick and x not in sick and times_contacted[y] <= k:
                sick.add(x)

        # Check if final state matches
        if sick == initial_state:
            valid_cows.add(pz)
            valid_k.append(k)

k_min = min(valid_k) if valid_k else 0
k_max = max(valid_k) if valid_k else 0

if k_max == 250:  # Use 250 as infinity threshold
    k_max = 'Infinity'

print(f'{len(valid_cows)} {k_min} {k_max}')
