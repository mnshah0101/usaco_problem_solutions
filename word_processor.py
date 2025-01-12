import sys

sys.stdin = open("word.in", "r")
sys.stdout = open("word.out", "w")

n, k = [int(x) for x in input().split()]
old_essay = [x for x in input().split()]




new_essay = ''


curr = 0 

for word in old_essay:
    if len(word) + curr > k:
        new_essay += '\n' + word
        curr = len(word)
    else:
        new_essay += ' ' + word
        curr += len(word)



print(new_essay.strip())

