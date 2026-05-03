# game.py

PLAYER_X = 'X'   # AI
PLAYER_O = 'O'   # opponent
EMPTY = ' '

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(board):
    win_pos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for i,j,k in win_pos:
        if board[i] == board[j] == board[k] and board[i] != EMPTY:
            return board[i]
    return None

def is_terminal(board):
    if check_winner(board) is not None:
        return True
    if EMPTY not in board:
        return True
    return False

def get_moves(board):
    moves = []
    for i in range(9):
        if board[i] == EMPTY:
            moves.append(i)
    return moves

def evaluate(board):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 10
    elif winner == PLAYER_O:
        return -10
    else:
        return 0
