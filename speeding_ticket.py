import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")


n, m  = [int(x) for x in input().split()]
limits = [0] * 100
speeds = [0] * 100


limits_list =[]
speeds_list = []
for i in range(n):
    limits_list.append([int(x) for x in input().split()])
for i in range(m):
    speeds_list.append([int(x) for x in input().split()])

i = 0
for length, speed in limits_list:
    original = i
    while i < original + length:
        limits[i] = speed
        i+= 1
i= 0
for length, speed in speeds_list:
    original = i
    while i < original + length:
        speeds[i] = speed
        i += 1

max_diff = 0
for i in range(len(speeds)):
    max_diff = max(max_diff, speeds[i] - limits[i])

print(max_diff)

