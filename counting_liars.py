from bisect import bisect_left, bisect_right

n = int(input().strip())

less = []
greater = []

for _ in range(n):
    t, p = input().split()
    p = int(p)
    if t == "G":
        greater.append(p)
    else:  # t == "L"
        less.append(p)

# Sort both lists
less.sort()
greater.sort()

min_lies = float('inf')

# Collect unique candidate "truth" values
candidates = set(less + greater)

for x in candidates:
    # Count how many "G p" are lies => those p where p > x
    g_lies = len(greater) - bisect_right(greater, x)

    # Count how many "L p" are lies => those p where p < x
    l_lies = bisect_left(less, x)

    total_lies = g_lies + l_lies

    if total_lies < min_lies:
        min_lies = total_lies

print(min_lies)
