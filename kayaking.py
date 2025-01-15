import sys

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')



input()

weights = [int(x) for x in input().split()]


weights.sort()
differences = [0] * (len(weights) - 1)

print(weights)

for i, weight in enumerate(weights[:-1]):

    differences[i] = abs(weights[i] - weights[i+1])


differences.sort()
differences = differences[::-1]

print(differences)


print(sum(differences[2:]))





   
    

    
