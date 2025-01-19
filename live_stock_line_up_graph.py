import sys
from collections import defaultdict
sys.stdin = open('lineup.in', 'r')
sys.stdout = open('lineup.out', 'w')

n = int(input())




cows_convert = {'Beatrice':0, 'Belinda':1,'Bella':2,'Betsy':3,'Bessie':4,'Blue':5, 'Buttercup':6, 'Sue':7}

cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy' ,'Blue', 'Buttercup', 'Sue']

cows_graph = defaultdict(set)

for _ in range(n):
    arr = input().split()
    cows_graph[arr[0]].add(arr[-1])
    cows_graph[arr[-1]].add(arr[0])

line_up = []
seen_cows = set()

for cow in cows:
    if cow in seen_cows:
        continue

    cows_len = len(cows_graph[cow])
    
    if cows_len == 2:
        continue

    if cows_len == 0:
        line_up.append(cow)
        seen_cows.add(cow)
        continue
    
    #this is a start of a chain
    stack = [cow]
    while stack:
        append_cow = stack.pop()
        cows_connected = cows_graph[append_cow]
        seen_cows.add(append_cow)
        line_up.append(append_cow)
        for connected in cows_connected:
            cows_graph[connected].remove(append_cow)
            if connected not in seen_cows:
                stack.append(connected)
                seen_cows.add(connected)


for cow in line_up:
    print(cow)

       
    

        







