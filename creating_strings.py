s = input()


permutation = []
curr = ''
seen = set()
n = len(s)
ret = set()

def search():
    if len(permutation) == n:
        ret.add(''.join(permutation[:]))
        return
    else:
        for i, c in enumerate(s):
            if i not in seen:
                seen.add(i)
                permutation.append(c)
                search()
                seen.remove(i)
                permutation.pop()
search()
ret = list(ret)
ret.sort()
print(len(ret))
for item in ret:
    print(item)
