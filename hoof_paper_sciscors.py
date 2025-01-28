import sys
sys.stdin = open('hps.in', 'r')
sys.stdout = open('hps.out', 'w')

n = int(input())

moves = []
for _ in range(n):
    moves.append(input())

prefix_hoof = [0] * n
prefix_scissors = [0] * n
prefix_paper = [0] * n

# Populate prefix arrays
for i in range(n):
    move = moves[i]
    if i > 0:
        prefix_hoof[i] = prefix_hoof[i - 1]
        prefix_scissors[i] = prefix_scissors[i - 1]
        prefix_paper[i] = prefix_paper[i - 1]

    if move == "P":
        prefix_paper[i] += 1
    elif move == "H":
        prefix_hoof[i] += 1
    elif move == "S":
        prefix_scissors[i] += 1

tracker = {'H': prefix_hoof, 'P': prefix_paper, 'S': prefix_scissors}

# Calculate maximum wins
max_wins = 0
arr = ['PH', 'HP', 'SP', 'PS', 'HS', 'SH']

for i in range(n):
    for pair in arr:
        j, p = pair
        j_val = tracker[j][i]
        p_val = tracker[p][n - 1] - tracker[p][i]
        max_wins = max(max_wins, j_val + p_val)

print(max_wins)
