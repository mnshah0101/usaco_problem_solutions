import sys

sys.stdin = open('circlecross.in', 'r')
sys.stdout = open('circlecross.out', 'w')

s = input().strip()

letters = [[0,0] for _ in range(26)] 
seen = set()

for i, letter in enumerate(s):
    if letter not in seen:
        letters[ord(letter) - ord("A")][0] = i
        seen.add(letter)
    else:
        letters[ord(letter) - ord("A")][1] = i


ans = 0
for i in range(len(letters)):
    for j in range(i + 1, len(letters)):
        first = letters[i]
        second = letters[j]
        if (first[0] < second[0] < first[1] < second[1]) or (second[0] < first[0] < second[1] < first[1]):
   
            ans += 1

print(ans)



