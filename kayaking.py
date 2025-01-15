import sys




input()

weights = [int(x) for x in input().split()]


weights.sort()

min_instability = float('inf')


#we can choose 2 randoms to be single
for i in range(len(weights)):
    for j in range(i+1, len(weights)):
        start = 0
        valid = []

        for n, weight in enumerate(weights):
            if n != i and n!=j:
                valid.append(weight)


        
        total_diff = 0
        for n in range(0,len(valid),2):
            total_diff += abs(valid[n]-valid[n+1])

        min_instability = min(min_instability, total_diff)


print(min_instability)







        


   
    

    
