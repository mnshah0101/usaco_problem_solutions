import sys

sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")

s = input().strip()
t = input().strip()

new_string = ''
for c in s:
    new_string += c
    if len(new_string) >= len(t):
        if new_string[-(len(t)):] == t:
            new_string = new_string[:-len(t)]

print(new_string)
