import sys
from collections import Counter

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")


n = int(input())

flats = input()


left = 0 
right = n - 1

c = Counter(flats)

while left < right:
    l = c[flats[left]]
    r = c[flats[right]]

    if l == 1 and r == 1:
        break
    
    if l > r:
        c[flats[left]] -= 1
        left += 1
    else:
        c[flats[right]] -=1
        right -= 1



print(right - left + 1)
    
