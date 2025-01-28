import sys
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')


n, k = [int(x) for x in input().split()]


sweep = []
for _ in range(k):
    a, b = [int(x) for x in input().split()]
    sweep.append((a,1))
    sweep.append((b,-1))

total = 0
heights = []
sweep.sort()
for a,b in sweep:
    total += b
    heights.append(total)


heights.sort()

print(heights[len(heights)//2])
