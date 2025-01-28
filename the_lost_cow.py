import sys

import sys

sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")


x,y  = [int(x) for x in input().split()]

direction = 1
increment = 1
distance = 0

while True:
    go_to = x + increment*direction
    if direction == 1 and x <= y <=go_to:
        distance += abs(y-x)
        break
    elif direction == -1 and go_to <= y <= x:
        distance += abs(y-x)
        break
    else:
        distance += abs(go_to - x) * 2
        increment *= 2
        direction *= -1

print(distance)

