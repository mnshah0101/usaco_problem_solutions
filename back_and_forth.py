import sys
sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')


barn1_buckets = set()
barn2_buckets = set()

barn1 = [int(x) for x in input().split()]

barn2 = [int(x) for x in input().split()]

barn1_buckets = barn1
barn2_buckets = barn2

readings = set()




def calculate_reading(arr):
    barn1 = 1000
    barn2 = 1000
    for i, bucket in enumerate(arr):
        if i%2:
            barn1 -= bucket
            barn2 += bucket
        else:
            barn1 += bucket
            barn2 -= bucket

    return barn1

def search(curr):
    if len(curr) == 4:
        readings.add(calculate_reading(curr))
        return
    i = len(curr)

    if i % 2 == 0:
        #this means we are going from barn 1 to 2
        for bucket in list(barn1_buckets):
            barn1_buckets.remove(bucket)
            barn2_buckets.add(bucket)
            curr.append(bucket)
            search(curr[:])
            curr.pop()
            barn2_buckets.remove(bucket)
            barn1_buckets.add(bucket)

    else:
        for bucket in list(barn2_buckets):
            barn2_buckets.remove(bucket)
            barn1_buckets.add(bucket)
            curr.append(bucket)
            search(curr[:])
            curr.pop()
            barn1_buckets.remove(bucket)
            barn2_buckets.add(bucket)

search([])

print(readings)

print(len(readings))


    
