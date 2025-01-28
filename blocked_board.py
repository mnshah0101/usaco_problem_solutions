#Just need to do cases
fin, fout = open("billboard.in"), open("billboard.out", "w")

x1, y1, x2, y2 = map(int, fin.readline().split())
x3, y3, x4, y4 = map(int, fin.readline().split())

# we'll be using one-indexing to make things more obvious
x = [0, x1, x2, x3, x4]
y = [0, y1, y2, y3, y4]

# Case 1
if x[4] >= x[2] and x[3] <= x[1] and y[4] >= y[2] and y[3] <= y[1]:
	fout.write(str(0))
# Case 2
elif x[3] <= x[1] and y[3] <= y[1] and y[4] > y[1] and x[4] >= x[2]:
	fout.write(str((x[2] - x[1]) * (y[2] - y[4])))
# Case 3
elif y[3] < y[2] and x[3] <= x[1] and y[4] >= y[2] and x[4] >= x[2]:
	fout.write(str((x[2] - x[1]) * (y[3] - y[1])))
# Case 4
elif x[4] > x[1] and x[3] <= x[1] and y[4] >= y[2] and y[3] <= y[1]:
	fout.write(str((x[2] - x[4]) * (y[2] - y[1])))
# Case 5
elif x[3] < x[2] and x[4] >= x[2] and y[4] >= y[2] and y[3] <= x[1]:
	fout.write(str((x[3] - x[1]) * (y[2] - y[1])))
# Case 6 and the corner case
else:
	fout.write(str((x[2] - x[1]) * (y[2] - y[1])))
