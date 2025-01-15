import sys
from collections import defaultdict
sys.stdin = open('lineup.in', 'r')
sys.stdout = open('lineup.out', 'w')

n = int(input())


next_to = defaultdict(set)

for i in range(n):
    pair = [x for x in input().split()]
    pair = (pair[0], pair[-1])
    next_to[pair[0]].add(pair[1])
    next_to[pair[1]].add(pair[0])


curr = []
line_ups = []

cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]


def create_line_ups():
    if len(curr) >= 8:
        line_ups.append(list(curr)[:])
        return
    else:
        for cow in cows:
            if cow not in curr:
                curr.append(cow)
                create_line_ups()
                curr.pop()
    

create_line_ups()
valid_list = []



for lineup in line_ups:
    is_valid = True
    for i, cow in enumerate(lineup):
        adj = next_to[cow]
        for a in adj:
            is_in = False
            if i and(a == lineup[i-1]):
                is_in = True
            if i < len(lineup)-1 and a== lineup[i+1]:
                is_in = True

            if not is_in:
                is_valid = False
           
            if not is_valid:
                break
        if not is_valid:
            break
    if not is_valid:
        continue

    if is_valid:
        valid_list.append(lineup)



valid_list.sort()
valid = valid_list[0]
for cow in valid:
    print(cow)

    



