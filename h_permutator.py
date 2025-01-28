
import sys

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')

n = int(input())


a  = [int(x) for x in input().split()]
b = sorted([int(x) for x in input().split()])[::-1]


new_arr = a
for i in range(len(a)):
    new_arr[i] = (i+1)*new_arr[i]*(n-i)

new_arr.sort()

ret = 0

for i, num in enumerate(new_arr):
    ret += num * b[i]

print(ret)



