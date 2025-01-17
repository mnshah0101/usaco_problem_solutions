#not complete
import sys
sys.stdin = open("hoofball.in", "r")
sys.stdout = open("hoofball.out", "w")

n = int(input())

arr = [int(x) for x in input().split()]

arr.sort()


balls = 1
just_added = False

for i in range(len(arr)):
    if not i or i == len(arr)-1:
        continue
    dist_left = arr[i] - arr[i-1]
    dist_right = arr[i+1] - arr[i]
    

    if dist_left <= dist_right and not just_added:
        balls += 1
        just_added = True
    else:
        just_added = False

print(balls)
