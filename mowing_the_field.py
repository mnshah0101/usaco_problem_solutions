import sys

sys.stdin = open('mowing.in', 'r')
sys.stdout = open('mowing.out', 'w')

seen = {}

steps = []

n = int(input())

nx, ny = 0,0

max_x = float('inf')
step = 0
for _ in range(n):
    d, v = input().split()
    v = int(v)
    for i in range(v):
        step += 1
        if d == 'N':
            nx, ny = nx, ny+1
        elif d == 'E':
            nx, ny = nx + 1, ny
        elif d == 'S':
            nx, ny = nx, ny - 1
        elif d == 'W':
            nx, ny = nx - 1, ny
        if (nx, ny) in seen:
            max_x = min(max_x, step - seen[nx,ny])

        seen[nx,ny] = step



if max_x == float('inf'):
    print(-1)
    sys.exit()
print(max_x)

        

        

        
    

x = float('-inf')

    






