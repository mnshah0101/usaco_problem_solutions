import sys
import heapq

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

n = int(input())
cows = []

# Read and store cows as (arrival_time, index, duration)
for i in range(n):
    a, dt = map(int, input().split())
    cows.append((a, i, dt))
cows.sort(key=lambda x: (x[0], x[1]))

longest_wait = 0

# not_started: cows that haven't begun processing, ordered by arrival time
not_started = cows[:]  # make a copy of the sorted list
# waiting: cows that have arrived and are waiting, ordered by seniority (index)
waiting = []

time = 0

while not_started or waiting:
    # If no cow is waiting, jump forward in time to the next cow's arrival.
    if not waiting:
        time = max(time, not_started[0][0])

    # Move all cows that have arrived by current time into the waiting heap.
    while not_started and not_started[0][0] <= time:
        a, idx, dt = heapq.heappop(not_started)
        # Push with key = seniority (idx), but keep arrival time for wait calculation.
        heapq.heappush(waiting, (idx, a, dt))

    # Process the next cow in waiting (with the smallest index/seniority).
    if waiting:
        idx, arrival, dt = heapq.heappop(waiting)
        # Calculate waiting time.
        wait_time = time - arrival
        longest_wait = max(longest_wait, wait_time)
        # Update the time after processing this cow.
        time += dt

print(longest_wait)
