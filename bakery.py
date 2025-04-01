import sys
# Input reading (you can uncomment file redirection if needed)
sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

n = int(input())

input()

test_cases = []

for j in range(n):
    curr = []
    N, tc, tm = [int(x) for x in input().split()]
    curr.append((N, tc, tm))
    for i in range(N):
        curr.append([int(x) for x in input().split()])
    test_cases.append(curr)
    if j < n-1:
        input()



def check(case, w):
    #we can check if we can make this with n moonies
    #lets 
    N, tc, tm = case[0]
    X = tc
    Y = tm
    lx, hx = max(1, X - w), min(X + Y - w - 1, X)
    for i in range(N):
            a, b, c = case[i+1]
            d = X + Y - w
            #we matchmatically see if any x can allow us to use this many moonies and fullfull everyones request
            
            if (b - a > 0):
                lx = max(lx, (-c + b * d + (b - a - 1)) // (b - a))
            elif (a - b > 0):
                hx = min(hx, (c - b * d) // (a - b))
            else:
                if (a * d > c):
                    return False
    return (lx <= hx)

for case in test_cases:

    N, tc, tm = case[0]
    X = tc
    Y = tm

    lo = 0
    hi = X + Y - 2
    
    
    while(hi > lo):
        mid = (lo + hi) // 2
        if (check(case, mid)):
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)




