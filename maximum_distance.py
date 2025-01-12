import math
n = int(input())

x_coordinates = [int(x) for x in input().split()]

y_coordinates = [int(x) for x in input().split()]



points = zip(x_coordinates, y_coordinates)


def distance(point1, point2):
    return (point1[0] -  point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


max_distance = 0

for i in range(len(points)):
    for j in range(i+1, len(points)):
        max_distance = max(max_distance, distance(points[i], points[j]))

print(max_distance)
