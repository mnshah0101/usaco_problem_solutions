import sys

sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

n = int(input())


measurements = []

for i in range(n):
    day, cow, m = input().split()
    measurements.append((int(day), cow, int(m)))


bessie = [7] * 100
mildred = [7] * 100
elsie = [7] * 100

changes = 0

current_winners = set(['Bessie', 'Mildred', "Elsie"])
current_max = 7

measurements.sort()


for day, cow, measurement in measurements:
    curr = 7
    if cow == 'Bessie':
        last = 7
        if day:
            last = bessie[day-1]
        bessie[day:] = [last + measurement] * (100-day)
    elif cow == "Mildred":
        last = 7
        if day:
            last = mildred[day-1]
        mildred[day:] = [last + measurement] * (100-day)
    elif cow == "Elsie":
        last = 7
        if day:
            last = elsie[day-1]
        elsie[day:] = [last + measurement] * (100-day)
    



for i in range(100):
    current_max = max(elsie[i], mildred[i], bessie[i])
    curr_set = set()
    if current_max == elsie[i]:
        curr_set.add('Elsie')
    if current_max == mildred[i]:
        curr_set.add('Mildred')
    if current_max == bessie[i]:
        curr_set.add("Bessie")
    
    if curr_set != current_winners:
        
        changes += 1

    current_winners = curr_set
    


print(changes)

