# capacity then amount
import sys
from collections import defaultdict
sys.stdin = open("art.in", "r")
sys.stdout = open("art.out", "w")


x_bounds = defaultdict(lambda : (float('inf'),float('-inf')))

y_bounds = defaultdict(lambda : (float('inf'), float('-inf')))

colors = list(range(1,10))


colors_seen = set()
colors_points = defaultdict(list)

rows = int(input())

matrix = []

for i in range(rows):
    matrix.append(list(input()))

r = len(matrix)
c = len(matrix[0])


for i in range(r):
    for j in range(c):
        color = int(matrix[i][j])
        if color:
            colors_points[color].append((i,j))
            colors_seen.add(color)
            y_bounds[color] = (min(y_bounds[color][0], j),
                               max(y_bounds[color][1], j))
            x_bounds[color] = (min(x_bounds[color][0], i),
                               max(x_bounds[color][1], i))
            

total = 0
for color in colors_seen:
    #try every possible starting color
    #make sure its not in any bounding box
    can_be_first = True
    #go through each bounding box
    for color_box in colors_seen:
        if color_box == color:
            continue
        x_min, x_max = x_bounds[color_box]
        y_min, y_max = y_bounds[color_box]

        for i,j in colors_points[color]:
            if x_min <= i <= x_max and y_min <= j <= y_max:
                can_be_first = False
                break
        if not can_be_first:
            break
    if can_be_first:
        total += 1
        
            
print(total)
            


            
