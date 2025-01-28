import sys

sys.stdin = open('cbarn.in','r')
sys.stdout = open('cbarn.out', 'w')


n = int(input())
r = []
for _ in range(n):
    r.append(int(input()))


min_distance = float('inf')
for i in range(len(r)):
    distance = 0

    for d in range(len(r)):
        index =(d + i)%len(r)
        distance += r[index] * d

    min_distance = min(min_distance, distance)

print(min_distance)
