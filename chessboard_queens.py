board = []
obstacles = set()

# Read 8 lines of input
for i in range(8):
    line = input().strip()
    row_arr = []
    for c in line:
        if c == '.':
            row_arr.append(1)  # 1 means free cell
        else:
            row_arr.append(0)  # 0 means obstacle
    board.append(row_arr)

# Optional: keep track of obstacles in a set if needed
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == 0:
            obstacles.add((i, j))

# Will hold the number of ways (or total queens placed if you adapt logic)
total = 0


def search(row):
    """
    Attempt to place a 'queen' in row 'row', and then recurse.
    If row == 8, we've placed queens in all rows successfully.
    """
    global total

    # If we've gone past the last row, it means we found a valid placement
    # for each of the 8 rows. You could increment total to count solutions:
    if row == len(board):
        total += 1
        return

    # Try each column for this row
    for col in range(len(board)):
        # If this cell is available (1 means free)
        if board[row][col] == 1:
            # We will place a queen here, and block out any conflicting cells
            changed_cells = []

            # 1) Mark the queen's position with something special (e.g. 2)
            board[row][col] = 2
            changed_cells.append((row, col))

            # 2) Block the column below this row
            for r in range(row+1, len(board)):
                if board[r][col] == 1:
                    board[r][col] = -1  # -1 will mean "blocked by a queen"
                    changed_cells.append((r, col))

            # 3) Block the diagonals going down-left and down-right
            # down-right diagonal
            r, c = row, col
            while True:
                r += 1
                c += 1
                if r >= len(board) or c >= len(board):
                    break
                if board[r][c] == 1:
                    board[r][c] = -1
                    changed_cells.append((r, c))

            # down-left diagonal
            r, c = row, col
            while True:
                r += 1
                c -= 1
                if r >= len(board) or c < 0:
                    break
                if board[r][c] == 1:
                    board[r][c] = -1
                    changed_cells.append((r, c))

            # 4) Recurse to place a queen in the next row
            search(row + 1)

            # 5) Revert the board to its previous state
            for (rr, cc) in changed_cells:
                # If we replaced 1 with -1 or 2, restore it to 1.
                # If the original was an obstacle (0), we wouldn't have changed it anyway,
                # so no risk of overwriting obstacles in this approach.
                board[rr][cc] = 1


# Start backtracking from row 0
search(0)

# Print how many solutions (or ways) we found
print(total)
