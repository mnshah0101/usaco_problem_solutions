import sys

sys.stdin = open('circlecross.in', 'r')
sys.stdout = open('circlecross.out', 'w')

s = input().strip()

open_set = set()
total_pairs = 0
tracker = {}

for c in s:
    if c in open_set:
        # We are seeing c for the second time, so close it
        open_set.remove(c)

        # Count how many currently open cows started after c was opened
        total_pairs += (len(open_set) - tracker[c])
    else:
        # We are seeing c for the first time, so open it
        tracker[c] = len(open_set)
        open_set.add(c)

print(total_pairs)
