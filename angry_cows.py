with open("angry.in") as read:
	bales = sorted([int(read.readline()) for _ in range(int(read.readline()))])


def exploded_num(start: int, direction: int) -> int:
	radius = 1
	prev = start
	while True:
		next_ = prev
		# Get the furthest explosion index without exceeding the current radius
		while (
			0 <= next_ + direction < len(bales)
			and abs(bales[next_ + direction] - bales[prev]) <= radius
		):
			next_ += direction

		# We didn't find a new haybale, so the chain explosion is over
		if next_ == prev:
			break

		# Update our previous explosion and increment radius
		prev = next_
		radius += 1
	return abs(prev - start)


max_exploded = 0
for i in range(len(bales)):
	# Get the number of exploded bales for the left & right side
	max_exploded = max(max_exploded, exploded_num(i, -1) + exploded_num(i, 1) + 1)
print(max_exploded, file=open("angry.out", "w"))
