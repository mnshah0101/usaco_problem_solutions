
numbers = [int(x) for x in input().split()]


numbers.sort()

a_b_c = numbers[-1]

a = numbers[0]
b = numbers[1]
c = a_b_c - (a+b)

print(f"{a} {b} {c}")
