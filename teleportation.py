import sys

sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")

a, b, x, y = [int(x) for x in input().split()]

#we want to transport a to b, but x to y gives us the teleporter

min_distance = abs(a-b)

#can either enter through x or y

enter_x = abs(a-x) + abs(y-b)
enter_y = abs(a-y) + abs(x-b)

min_distance = min(min_distance, enter_x, enter_y)

print(min_distance)

