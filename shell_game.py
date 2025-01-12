import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

#simulate
swaps = int(input())


swap_list = []


for i in range(swaps):
    swap_list.append([int(x) for x in input().split()])




max_points = 0

#check each starting point
for initial in range(1,4):
    curr_points = 0
    at = initial
    matches = []
    for a, b, guess in swap_list:
      
        if a == at:
            at = b
        elif b == at:
            at = a
        if guess == at:
            curr_points += 1
            matches.append(at)
        
    max_points = max(max_points, curr_points)


print(max_points)






