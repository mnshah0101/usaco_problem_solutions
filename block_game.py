import sys

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")


n = int(input())


blocks = []

for i in range(n):
    blocks.append([x for x in input().split()])

c = [0] * 26

def getIndex(letter):
    return ord(letter) - 97


for word1, word2 in blocks:
    word_one_counts = [0] * 26
    word_two_counts = [0] * 26
    for letter in word1:
        word_one_counts[getIndex(letter)] += 1
    for letter in word2:
        word_two_counts[getIndex(letter)] += 1

    for i in range(26):
        c[i] += max(word_one_counts[i], word_two_counts[i])

for i in c:
    print(i)







