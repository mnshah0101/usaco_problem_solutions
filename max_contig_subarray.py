import sys

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')

n = int(input())

arr = [int(x) for x in input().split()]


prefix_sum  = arr

prefix_sum = prefix_sum

for i in range(len(prefix_sum)):
    if i:
        prefix_sum[i] += prefix_sum[i-1]

min_i = 0

max_sum = 0


for i, num in enumerate(prefix_sum):
    

    max_sum = max(max_sum, num - min_i)
    min_i = min(min_i, num)
    
print(max_sum)
