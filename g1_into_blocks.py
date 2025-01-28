

import sys
from collections import defaultdict, Counter


n, q = [int(x) for x in input().split()]

old_arr = [int(x) for x in input().split()]

counter = defaultdict(lambda : (float('inf'),float('-inf')))


for i, num in enumerate(old_arr):

    counter[num] =( min(counter[num][0], i), counter[num][1])
    counter[num] =(counter[num][0],max(counter[num][1], i))


arr = [(x[0],x[1]) for x   in counter.values()]

arr.sort()


prev = arr[0]

merged_intervals = []


for i in range(len(arr)):
    if not i:
        continue
    curr = arr[i]
  

    if curr[0] > prev[1]:
        merged_intervals.append(prev)
        prev = curr
    elif curr[0] < prev[1]:
        prev = (prev[0], max(prev[1] , curr[1]))
    

merged_intervals.append(prev)

merged_intervals.sort()

differences = 0

for i,j in merged_intervals:
    #both are inclusive
    c = Counter(old_arr[i:j+1])
    c_values = sorted(c.values())
    differences += sum(c_values) - c_values[-1] 

print(differences)

