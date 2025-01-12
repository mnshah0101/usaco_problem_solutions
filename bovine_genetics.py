import sys
sys.stdin = open('cownomics.in', 'r')
sys.stdout = open('cownomics.out', 'w')

spotty, n = [int(x) for x in input().split()]

spotty_cows = []

for i in range(spotty):
    spotty_cows.append(input())

cows = []
while True:
    try:
        i = input()
        cows.append(i)
    except:
        break
    
potential_spots = 0
for i in range(n):
    spotty_set = set()
    cow_set = set()
    for cow in spotty_cows:
        spotty_set.add(cow[i])
    for cow in cows:
        cow_set.add(cow[i])

    if len(spotty_set.intersection(cow_set)) == 0:
        potential_spots += 1


print(potential_spots)



