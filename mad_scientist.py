import sys
sys.stdin = open('breedflip.in', 'r')
sys.stdout = open('breedflip.out', 'w')
n = int(input())
s1 = input()
s2 = input()

i = 0

total_number = 0

while i < n:

    if s1[i] == s2[i]:
        i += 1
        continue
    
    total_number += 1
    while i<n and s1[i] != s2[i]:
        i += 1
    

print(total_number)
