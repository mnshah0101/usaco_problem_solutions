import sys
from collections import Counter

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')


num_test_cases = int(input())


test_cases = []
for _ in range(num_test_cases):
    n,m = [int(x) for x in input().split()]

    case = [int(x) for x in input().split()]
    case.sort()
    test_cases.append((n,m,case))
    



for n, m, case in test_cases:
    left = 0
    c = Counter()
    min_case = float('inf')
    for right in range(len(case)):
        a = case[right]
        max_factor = m
        needed_factors = set(list(range(1,m+1)))
        for factor in range(1,max_factor+1):
            if a % factor == 0:
                c[factor]+= 1
        
        #shrink
        while set(list(c.keys())) == needed_factors:
            min_case = min(abs(case[right]-case[left]), min_case)
        
            a = case[left]
            max_factor = m 
            for factor in range(1,max_factor+1):
                if a % factor == 0:
                    c[factor]-= 1
                    if c[factor] == 0:
                        del c[factor]
            left += 1
    if min_case == float('inf'):
        print(-1)
    else:
        print(min_case)
        











