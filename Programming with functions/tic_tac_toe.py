X = "x"
O = "o"
SPACE = " "

board = [
    #  0     1       2
    [SPACE, SPACE, SPACE], # row 0
    [SPACE, SPACE, SPACE], # row 1
    [SPACE, SPACE, SPACE] # row 2
]
#board[row][col]



def display(board):
    for row in range(3):
        for col in range(3):
            print(f" {board[row][col]} ", end="")
            if col != 2:
                print("|", end="")
        print()
        if row != 2:
            print("---+---+---")

def is_game_over_nospaces(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == SPACE:
                return False

def is_game_over_xo(board, sym):
    for row in range(3):
        if board[row].count(sym) == 3:
            return True
        
    for col in range(3):
        if board[0][col] == sym and board[1][col] == sym and board[2][col] == sym:
            return True
        
    if board[0][0] == sym and board[1][1] == sym and board[2][2] == sym:
            return True
    if board[2][0] == sym and board[1][1] == sym and board[0][2] == sym:
            return True
    
    return False
        
def is_game_over(board):
    if is_game_over_nospaces(board):
        return True
    if is_game_over_xo(board, X):
        return True
    if is_game_over_xo(board, O):
        return True

display(board)