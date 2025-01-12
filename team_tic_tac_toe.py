import sys

sys.stdin = open("tttt.in", "r")
sys.stdout = open("tttt.out", "w")



board  = []

for i in range(3):
    board.append(list(input()))


single_set = set()

for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
        single_set.add(board[i][0])
    if board[0][i] == board[1][i] == board[2][i]:
        single_set.add(board[0][i])
    
if board[0][0] == board[1][1] == board[2][2]:
    single_set.add(board[0][0])
if board[0][2] == board[1][1] == board[2][0]:
    single_set.add(board[1][1])


print(len(single_set))


double_set = set()

for i in range(3):
    if len(set(board[i])) == 2:
        double_set.add(str(sorted(''.join(list(set(board[i]))))))

    vertical_set = set([board[0][i], board[1][i],board[2][i]])
    if len(vertical_set) == 2:
        double_set.add(str(sorted(''.join(list(vertical_set)))))
    

diagnol_set = set([board[0][0], board[1][1], board[2][2]])
if len(diagnol_set) == 2:
    double_set.add(str(sorted(''.join(list(diagnol_set)))))

other_diagnol_set = set([board[0][2], board[1][1], board[2][0]])
if len(other_diagnol_set) == 2:
    double_set.add(str(sorted(''.join(list(other_diagnol_set)))))


print(len(double_set))
