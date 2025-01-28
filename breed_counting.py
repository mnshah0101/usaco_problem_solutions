import sys
sys.stdin = open('bcount.in', 'r')
sys.stdout = open('bcount.out', 'w')
n,q  =[int(x) for x in input().split()]

breeds = []
curr = [0,0,0]
for _ in range(n):
    
    breeds_idx = int(input()) - 1
    curr[breeds_idx] += 1
    breeds.append(curr[:])




queries = []
for _ in range(q):
    queries.append([int(x) for x in input().split()])

for a,b in queries:
    a -= 2
    b -= 1
    a_h,  a_g, a_j = 0,0,0
    if a >= 0:
        a_h,  a_g, a_j = breeds[a]
    b_h,  b_g, b_j = breeds[b]
    print(f'{b_h - a_h} {b_g - a_g} {b_j - a_j}')

