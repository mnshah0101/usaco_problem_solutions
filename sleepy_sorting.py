import sys

sys.stdin = open("sleepy.in", "r")
sys.stdout = open("sleepy.out", "w")

n = int(input())

cows = [int(x) for x in input().split()]

if len(cows) == 1:
    print(0)
    sys.exit()


max_unsorted = 0

for i in range(len(cows)-1):
    if cows[i] > cows[i+1]:
        max_unsorted = i
print(max_unsorted+1)
