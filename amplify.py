import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

matrix = []

m, n, k = [int(x) for x in input().split()]


for i in range(m):
    matrix.append(input())


ret = []

for line in matrix:
    append_string = ''
    for char in line:
        for i in range(k):
            append_string += char
    for i in range(k):
        ret.append(append_string)

for line in ret:
    print(line)

    
