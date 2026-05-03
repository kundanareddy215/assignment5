# mcts.py

import random
from game import *

def random_playout(board, player):

    current = player

    while not is_terminal(board):
        move = random.choice(get_moves(board))
        board[move] = current

        if current == PLAYER_X:
            current = PLAYER_O
        else:
            current = PLAYER_X

    winner = check_winner(board)

    if winner == PLAYER_X:
        return 1
    elif winner == PLAYER_O:
        return -1
    else:
        return 0


def mcts(board, iterations=500):

    scores = {}

    for move in get_moves(board):
        scores[move] = 0

        for _ in range(iterations):
            temp = board[:]
            temp[move] = PLAYER_X

            result = random_playout(temp, PLAYER_O)
            scores[move] += result

    best_move = max(scores, key=scores.get)
    return best_move
