import sys

sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")


miles = []

n = int(input())


for i in range(n):
    miles.append([x for x in input().split()])
    t, in_, o = miles[i]
    in_ = int(in_)
    o = int(o)
    if t== 'on':
        t = 1
    elif t== 'off':
        t = -1
    else:
        t = 0
    miles[i] = (t, in_, o)

low = 0
high = float('inf')
for t, s, e in miles[::-1]:
    #none case
    if t == 0:
        low = max(low, s)
        high = min(high, e)
    elif t == -1:
        low += s
        high += e
    elif t == 1:
        low -= e
        high -= s
        low = max(0, low)


print(f'{low} {high}')


low = 0
high = float('inf')
for t, s, e in miles:
    # none case
    if t == 0:
        low = max(low, s)
        high = min(high, e)
    elif t == 1:
        low += s
        high += e
    elif t == -1:
        low -= e
        high -= s
        low = max(0, low)


print(f'{low} {high}')





