import math
from game import *

def minimax(board, isMax):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if is_terminal(board):
        return 0

    if isMax:
        best = -math.inf

        for move in get_moves(board):
            board[move] = PLAYER_X
            val = minimax(board, False)
            board[move] = EMPTY
            best = max(best, val)

        return best

    else:
        best = math.inf

        for move in get_moves(board):
            board[move] = PLAYER_O
            val = minimax(board, True)
            board[move] = EMPTY
            best = min(best, val)

        return best


def best_move_minimax(board):
    best_val = -math.inf
    best_move = -1

    for move in get_moves(board):
        board[move] = PLAYER_X
        move_val = minimax(board, False)
        board[move] = EMPTY

        if move_val > best_val:
            best_val = move_val
            best_move = move

    return best_move
