import sys
#for smallest string concat
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')
class CompString:
    def __init__(self, s):
        self.s = s
    def __str__(self):
        return self.s
    def __lt__(self, other):
        return (str(self.s) + str(other)) < (str(other) + str(self.s))



    
n = int(input())


words = []
for _ in range(n):
    words.append(CompString(input()))

words.sort()

print(''.join([word.s for word in words]))
