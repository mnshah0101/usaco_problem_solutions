import sys
from math import gcd
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')


n = int(input())
arr = [int(x) for x in input().split()]



prefix_gcd = [0] * n
prefix_gcd[0] = arr[0]

suffix_gcd = [0] * n
suffix_gcd[n - 1] = arr[n - 1]


for i in range(1, n):
    prefix_gcd[i] = gcd(prefix_gcd[i-1], arr[i])

for i in range(n-2, -1, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i+1], arr[i])

#lets see if we can replace between 1 and n-2
ans = 0
for i in range(1, n-2):
    ans = max(ans, gcd(suffix_gcd[i+1], prefix_gcd[i-1]))

#lets see if we should replace the 1st one

ans = max(ans, suffix_gcd[1])

#lets see if we should replace the last one
ans = max(ans, prefix_gcd[n-2])


print(ans)



