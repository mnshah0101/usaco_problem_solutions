import sys
from collections import defaultdict

sys.stdin = open("notlast.in", "r")
sys.stdout = open("notlast.out", "w")

arr = []

n = int(input())

output = defaultdict(int)

for _ in range(n):
    cow, i = input().split()
    output[cow] += int(i)





sorted_arr = sorted(output.items(), key = lambda x : x[1])
if len(sorted_arr) < 2:
    print("Tie")
    sys.exit()

initial_cow, initial_output = sorted_arr[0]


for i,entry in enumerate(sorted_arr):
    if not i:
        continue
    cow, num = entry
    if initial_output == num:
        continue

    if i + 1 < len(sorted_arr) and sorted_arr[i+1][1] == sorted_arr[i][1]:
        print('Tie')
        break
    
    print(cow)
    break





