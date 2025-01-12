#capacity then amount
import sys

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")


milk_amounts = []

for i in range(3):
    milk_amounts.append([int(x) for x in input().split()])

for i in range(100):
    operation = i%3
    if operation == 0:
        capacity = milk_amounts[1][0] - milk_amounts[1][1]
        removed = min(milk_amounts[0][1], capacity)
        milk_amounts[1][1] += removed
        milk_amounts[0][1] -= removed
    elif operation == 1:
       capacity = milk_amounts[2][0] - milk_amounts[2][1]
       removed = min(milk_amounts[1][1], capacity)
       milk_amounts[2][1] += removed
       milk_amounts[1][1] -= removed
    else:
       capacity = milk_amounts[0][0] - milk_amounts[0][1]
       removed = min(milk_amounts[2][1], capacity)
       milk_amounts[0][1] += removed
       milk_amounts[2][1] -= removed


print(milk_amounts[0][1])
print(milk_amounts[1][1])
print(milk_amounts[2][1])


       
      

