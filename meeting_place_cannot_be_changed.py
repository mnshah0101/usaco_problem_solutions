num_friends = int(input())
friend_coords = list(map(int, input().split()))
friend_veloci = list(map(int, input().split()))

"""
can binary search on all times
"""

def all_friends_converge(seconds: int) -> bool:
	"""
	Checks whether all friends can converge on one point in the specified time interval.

	:param seconds: Amount of seconds given for friends to converge.
	:return: If the friends can converge to a single point.
	"""

	overlap_lower, overlap_upper = 1, 10**9
	for i in range(num_friends):
		lower_bound = friend_coords[i] - (friend_veloci[i] * seconds)
		upper_bound = friend_coords[i] + (friend_veloci[i] * seconds)
		if lower_bound > overlap_upper or upper_bound < overlap_lower:
			return False
		if lower_bound > overlap_lower:
			overlap_lower = lower_bound
		if upper_bound < overlap_upper:
			overlap_upper = upper_bound
	return True


left, right = 0, 10**9
diff = 10**-6

while left + diff < right:
	mid = (left + right) / 2
	last_comparison = all_friends_converge(mid)
	if last_comparison:
		right = mid
	else:
		left = mid + diff

# We make our output slightly more accurate
print(((left + mid) / 2) if last_comparison else ((mid + right) / 2))
