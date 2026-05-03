from minimax import best_move_minimax
from alpha_beta import best_move_alpha_beta
from mcts import mcts

# test 1
board1 = ['X','O','X',
          ' ','O',' ',
          ' ',' ','X']

# test 2
board2 = ['O','O',' ',
          'X',' ',' ',
          ' ',' ','X']

# test 3
board3 = [' '] * 9

print("Minimax:", best_move_minimax(board1))
print("Alpha-Beta:", best_move_alpha_beta(board1))
print("MCTS:", mcts(board1))
