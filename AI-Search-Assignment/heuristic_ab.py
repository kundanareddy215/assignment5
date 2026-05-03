import math
from game import *

def heuristic(board):
    score = 0

    lines = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for i,j,k in lines:
        line = [board[i], board[j], board[k]]

        if line.count(PLAYER_X) == 2 and line.count(EMPTY) == 1:
            score += 5

        if line.count(PLAYER_O) == 2 and line.count(EMPTY) == 1:
            score -= 5

    return score


def alpha_beta_heuristic(board, depth, alpha, beta, isMax, max_depth):

    if is_terminal(board):
        return evaluate(board)

    if depth == max_depth:
        return heuristic(board)

    if isMax:
        best = -math.inf

        for move in get_moves(board):
            board[move] = PLAYER_X
            val = alpha_beta_heuristic(board, depth+1, alpha, beta, False, max_depth)
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
            val = alpha_beta_heuristic(board, depth+1, alpha, beta, True, max_depth)
            board[move] = EMPTY

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best
