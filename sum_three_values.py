import sys

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")


n, t = [int(x) for x in input().split(' ')]
arr = [(int(x), i+1) for i, x in enumerate(input().split(' '))]



arr.sort()


found = False
for i in range(len(arr[:-2])):
    left = i+ 1
    right  = i + 2

    while left < right:
        total = arr[left][0] + arr[right][0] + arr[i][0]
        if total == t:
            print(f'{arr[i][1]} {arr[left][1]} { arr[right][1]}')
            found = True
            break
        elif total > t:
            right -= 1
        else:
            left += 1

    if found:
        break

if not found:
    print("IMPOSSIBLE")



