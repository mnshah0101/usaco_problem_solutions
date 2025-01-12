import sys

sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

num_comps, num_cows = [int(x) for x in input().split()]

rankings = {}



for i in range(num_comps):
    my_dict = {}
    rank_line = [int(x) for x in input().split()]
    for rank, cow in enumerate(rank_line):
        my_dict[cow] = rank
    rankings[i] = my_dict
    

adjacent_pairs = 0


for i in range(1, num_cows+1):
    for j in range(i+1, num_cows+1):
        isConsistentGreater = True
        isConsistentLess = True
        for comp in range(num_comps):
            if rankings[comp][i] > rankings[comp][j]:
                isConsistentGreater = False
            if rankings[comp][i] < rankings[comp][j]:
                isConsistentLess = False
            if not isConsistentLess and not isConsistentGreater:
                break
        adjacent_pairs += int(isConsistentGreater) + int(isConsistentLess)

print(adjacent_pairs)





