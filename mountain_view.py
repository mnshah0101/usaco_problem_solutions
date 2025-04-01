class Mountain:
	def __init__(self, start: int, end: int):
		self.start = start
		self.end = end

	def __lt__(self, other):
		# sort by start and tiebreak by putting the larger mountains first
		if self.start == other.start:
			return self.end > other.end
		return self.start < other.start


with open("mountains.in") as read:
	mountain_num = int(read.readline())
	mountains = []
	for _ in range(mountain_num):
		x, y = [int(i) for i in read.readline().split()]
		# store the mountains by the interval they cover
		mountains.append(Mountain(x - y, x + y))

mountains.sort()

rightmost = -1
visible_num = 0
for m in mountains:
	if m.end > rightmost:
		visible_num += 1
		rightmost = m.end

print(visible_num, file=open("mountains.out", "w"))
