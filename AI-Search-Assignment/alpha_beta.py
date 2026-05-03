# alpha_beta.py

import math
from game import *

def alpha_beta(board, alpha, beta, isMax):

    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if is_terminal(board):
        return 0

    if isMax:
        best = -math.inf

        for move in get_moves(board):
            board[move] = PLAYER_X
            val = alpha_beta(board, alpha, beta, False)
            board[move] = EMPTY

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for move in get_moves(board):
            board[move] = PLAYER_O
            val = alpha_beta(board, alpha, beta, True)
            board[move] = EMPTY

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


def best_move_alpha_beta(board):
    best_val = -math.inf
    best_move = -1

    for move in get_moves(board):
        board[move] = PLAYER_X
        move_val = alpha_beta(board, -math.inf, math.inf, False)
        board[move] = EMPTY

        if move_val > best_val:
            best_val = move_val
            best_move = move

    return best_move
