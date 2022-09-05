from ColorChalks import ColorChalks

N = 9
def print_board(board):
    for i in range(9):
        for j in range(9):
            print([board[i][j]], end="")
        print()


# a function to check if its possible to place a number in given position or not
def possible(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
        
        if board[x][col] == num:
            return False
    
    # Check for 3 x 3 matrix
    startrow = row - row % 3
    startcol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startrow][j + startcol] == num:
                return False
    
    return True

def solve(board, row, col): 
    if(row == N - 1 and col == N):
        return True
    
    if col == N: 
        row += 1
        col = 0

    ## if col is not empty, then move on to next col
    if board[row][col] != 0:
        return solve(board, row, col+1)
    
    for num in range(1, N + 1):
        if possible(board, row, col, num) == True: 
            board[row][col] = num
            if solve(board, row, col+1):
                    return True
        board[row][col] = 0
    
    return False


l = list();
board = list()
print(ColorChalks.FCOLORS.Blue + "Enter Rows of sudoku board (0 for empty places) i.e. 100200090")
for i in range(9):
    print(ColorChalks.FCOLORS.Yellow + "EnterRow", i + 1)
    n = str(input("\n: "))
    l.append(n)
for x in l:
    n = [*x]
    board.append(n)
for y in range(9):
    for w in range(9):
        board[y][w] = int(board[y][w])
for rows in range(9): 
    print(board[rows])


if (solve(board, 0, 0)):
    print(ColorChalks.FCOLORS.Green + "\nSolution: ")
    print_board(board)
else: 
    print("no soluiton")