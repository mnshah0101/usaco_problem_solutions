from itertools import combinations
n,m = [int(x) for x in input().split()]

cows = []
aircons = []
for i in range(n):
    to_append = [int(x) for x in input().split()]
    cows.append(to_append)
for i in range(m):
    to_append = [int(x) for x in input().split()]
    aircons.append(to_append)

#stall si to ti and needs temp reduced by ci
#cows store si, ti, ci
#cools stalls ai to bi by pi and costs mi to operate

#cons stores ai, bi, pi, mi


#build all possible combination of stalls that span

combos = []

cows_stalls = [0] * 101

for s,t,c in cows:
    for i in range(s,t+1):
        cows_stalls[i] = c

def spans(arr):
    my_range = [0] * 101
    for a, b, p, m in arr:
        for i in range(a,b+1):
            my_range[i] += p
    
    for i in range(1,101):
        if cows_stalls[i] > my_range[i]:
            return False
        
    return True


def build(curr, i):
    if i >= len(aircons):
        if spans(curr):
            combos.append(curr[:])
        return
    else:
        curr.append(aircons[i])
        build(curr, i+1)
        curr.pop()
        build(curr, i+1)


#possible aircons stored in combos

build([],0)

min_val = float('inf')


for combo in combos:
    total = sum(m for a, b, p, m in combo )
    min_val = min(total, min_val)

print(min_val)



