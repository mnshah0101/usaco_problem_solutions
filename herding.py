import sys

sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

#if already, than min is 0
#if gap 2, then min is 1
#else can do in 2

#max is if we take the largest gap and keep iterating between it


a, b, c = map(int, input().split())

# Best scenario: the three elements are already in order.
if c == a + 2:
	print(0)

elif b == a + 2 or c == b + 2:
	print(1)

else:
	print(2)

print(max(b - a, c - b) - 1)
