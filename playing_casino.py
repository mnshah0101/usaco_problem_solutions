from collections import defaultdict

n_tests = int(input())

tests = []
test_numbers = []



for i in range(n_tests):
    n, m = [int(x) for x in input().split()]
    test_numbers.append((n,m))
    #n is the number of cards in each deck and m is the number of numbers on each card
    cards = []
    for i in range(n):
        cards.append([int(x) for x in input().split()])
    tests.append(cards)

for test_num in range(n_tests):
    n, m = test_numbers[test_num]
    matrix = tests[test_num]

    columns = defaultdict(list)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            columns[j].append(matrix[i][j])

    total = 0


    for col in range(len(matrix[0])):
        columns[col].sort()
        column = columns[col]
        games = len(matrix) - 1
     

        for row in range(len(matrix)):


            add = (column[row] * row) + (-1 * column[row] * (games-row))
            total += add

    
    print(total)

    
    
   
    




