n, k = map(int, input().split())
days = list(map(int, input().split()))

last_day = days[0]
cost = k + 1  # Start the first subscription

for d in days:
	# Should Bessie extend the most recent subscription?
	if d - last_day < k + 1:
		cost += d - last_day
	else:
		# Or just start a new one entirely?
		cost += k + 1

	# Store the date of the last subscription
	last_day = d

print(cost)
