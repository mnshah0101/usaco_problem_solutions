import sys

sys.stdin = open("whereami.in", "r")
sys.stdout = open("whereami.out", "w")

n  = int(input())

s = input()

for i in range(1, n):
    found = True
    tracker = set()
    for start in range(n-i+1):
        if s[start:start+i] in tracker:
            found = False
            break
        else:
            tracker.add(s[start:start+i])
    
    if found:
        print(i)
        break

if not found:
    print(n)
