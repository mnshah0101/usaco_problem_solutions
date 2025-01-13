import sys

sys.stdin = open('balancing.in', 'r')
sys.stdout = open('balancing.out', 'w')


#brute force go through each x,y 

n,b = [int(x) for x in input().split()]



pairs = []
fence_y = set()
fence_x = set()

for i in range(n):
    to_add = tuple([int(x) for x in input().split()])
    pairs.append(to_add)
    fence_x.add(to_add[0] + 1)

    fence_y.add(to_add[1] + 1)


m = float('inf')

#lets consider every x value, then every y value inside
for i in fence_x:
    for j in fence_y:
        #we consider every possible pair
        tl, tr, br, bl = 0, 0, 0, 0
        for x,y in pairs:
            if x < i and y < j:
                bl += 1
            if x < i and y > j:
                tl += 1
            if x > i and y > j:
                tr += 1
            if x > i and y < j:
                br += 1

        curr_m = max(tl, tr, br, bl)
        m = min(m, curr_m)


print(m)


        
    