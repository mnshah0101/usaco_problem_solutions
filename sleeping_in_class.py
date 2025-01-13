

t = int(input())

test_cases = []

for i in range(t):
    l = int(input())
    curr_list = [int(x) for x in input().split()]
    test_cases.append(curr_list)


#for each test case, go through valid num_hours, valid range is 0, total_sum

def print_for_each_case(arr):
    total_sum = sum(arr)

    
    for h in range(0, total_sum+1):
        if max(arr) == 0:
            print(0)
            return
        if h and total_sum%h != 0:
            continue
        curr_sum = 0
        
        #basically check we went through the whole thing
        for i, num in enumerate(arr):
            curr_sum += num
            if curr_sum > h:
                break
            if curr_sum == h:
                curr_sum = 0
        else:
            print(len(arr) - total_sum//h)
            return
                
        




for case in test_cases:
    print_for_each_case(case)
