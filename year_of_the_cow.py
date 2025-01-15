

n = int(input())


cows = []

for _ in range(n):
    new, _, _, t, y, _, _, p = input().split()
    cows.append((new,t,y,p))


years = {
    "Ox":1, "Tiger":2, "Rabbit":3, 'Dragon':4, "Snake":5, "Horse":6, "Goat":7, "Monkey":8, "Rooster":9, "Dog":10, "Pig":11, "Rat":12
}

cows_tracker = {}

def getYearDiff(p, t, y):
    """
    p is the name of the old person
    t is the type
    y is the year type
    """
    p_diff, born = cows_tracker[p]
    if t == 'previous':

        #if new person was born cycle before old person
        if years[y] >= years[born]:
            return -1* (12 - (years[y] - years[born]))
        
        else:
            return -1 * (years[born] - years[y])
    elif t == 'next':

        if years[y] > years[born]:
            return years[y] - years[born]
        
        else:
            return 12 - (years[born] - years[y])
        

cows_tracker['Bessie'] = (0,"Ox")

for new, t, y, p in cows:
    diff = getYearDiff(p,t, y)
    cows_tracker[new] = (diff + cows_tracker[p][0], y)


print(abs(cows_tracker['Elsie'][0]))






        

        




