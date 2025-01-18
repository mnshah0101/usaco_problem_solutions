import sys

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")


odd = 0
even = 0

n = int(input())

nums = [int(x) for x in input().split()]

print(nums)

for num in nums:
    if num%2 == 0:
        even += 1
    else:
        odd += 1

total = 0
if odd == even:
    sys.exit()

#we want to get rid of odds by combing two odd groups into an even group
while odd > even:
    odd -=2
    even += 1

#we can group evens by combining evens
if even > odd:
    even = odd + 1

print(f'Odd: {odd}')
print(f'Even: {even}')
print(odd + even)

