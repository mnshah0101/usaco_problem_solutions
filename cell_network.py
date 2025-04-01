import sys

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")


n,m = [int(x) for x in input().split()]

cities = [int(x) for x in input().split()]
reverse_cities = cities[::-1]
towers = [int(x) for x in input().split()]
reverse_towers = towers[::-1]



def test_works(r):
    l_t_r = set()
    r_t_l = set()

    
    curr_tower = 0

    for i in range(len(cities)):
        city = cities[i]
        if curr_tower < len(towers) - 1 and abs(towers[curr_tower] - city) >  abs(towers[curr_tower+1] - city):
            curr_tower += 1
        tower = towers[curr_tower]

        if abs(city - tower) > r:
            l_t_r.add(city)




    curr_tower = len(towers) - 1


    for i in range(len(cities)):
        city = reverse_cities[i]
        if curr_tower < len(towers) - 1 and abs(reverse_towers[curr_tower] - city) >  abs(reverse_towers[curr_tower+1] - city):
            curr_tower += 1
        tower = reverse_towers[curr_tower]

        if abs(city - tower) > r:
            r_t_l.add(city)

    
    for city in r_t_l:
        if city in l_t_r:
            return False

    return True


max_dist = 0
for i in range(1,len(cities)):
    max_dist = max(max_dist, cities[i] - cities[i-1])


left = 1
right = max_dist

while left < right:
    mid = (left+right) //2

    works = test_works(mid)

    if works:
        right = mid
    else:
        left = mid + 1 


print(left)
        



