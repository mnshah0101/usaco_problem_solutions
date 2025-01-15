import sys
from collections import defaultdict

sys.stdin = open("citystate.in", "r")
sys.stdout = open("citystate.out", "w")

# Dictionary to count occurrences of pairs (city prefix, state)
pair_count = defaultdict(int)

n = int(input())

# Read input and populate the pair_count dictionary
for _ in range(n):
    city, state = input().split()
    city_prefix = city[:2]  # First two letters of the city
    if city_prefix != state:  # Avoid same state-city pairs
        pair_count[(city_prefix, state)] += 1

# Count the number of special pairs
special_pairs = 0

for (city_prefix, state), count in pair_count.items():
    # Look for reverse pairs (state, city_prefix)
    reverse_pair = (state, city_prefix)
    if reverse_pair in pair_count:
        # Each occurrence of the pair matches with occurrences of its reverse
        special_pairs += count * pair_count[reverse_pair]

# Each pair is counted twice, so divide by 2
print(special_pairs // 2)
