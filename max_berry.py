import itertools
import random
import sys
sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")


"""
we want all the baskets to have approxiamtely the same number of berries

so how do we know we can do that?

lets try to see if we can fit anywhere from 1 to max berries in any bucket

"""

ans = 0

n, k = [int(x) for x in input().split()]

trees = [int(x) for x in input().split()]

for b in range(1,max(trees) + 1):
    mod = b
    full_b = 0
    tmp = 0
    for i in range(n):
        full_b += trees[i] // mod
    
    if full_b < k//2:
            break
    
	#if there are equal to k or greater we can allocate the leftovers
    if full_b >= k:
         ans = max(ans, (k//2) * i)
         continue
	

    idx = (full_b - k//2) * i
    
	#we get the rest of the berries from the trees
    while tmp < (k-full_b):
        if tmp < len(trees):

              idx += (trees[tmp]%b)
              tmp +=1
        else:
             break
    ans = max(ans, idx)
print(ans)
	    
         
    

        

        
    

