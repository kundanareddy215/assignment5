## Test Cases

Three test cases were used to verify the correctness of the algorithms:

* **Winning Scenario** – The algorithm selects a move that leads to a win.
* **Blocking Scenario** – The algorithm prevents the opponent from winning.
* **Empty Board** – The algorithm chooses an optimal starting move.

## Observations

* Alpha-Beta pruning is faster than Minimax due to reduced search space.
* Heuristic Alpha-Beta is useful for deeper searches where full exploration is not feasible.
* Monte Carlo Tree Search (MCTS) produces good results but may vary because of randomness.

## Conclusion

This project demonstrates how different AI search algorithms perform in decision-making problems. It highlights the trade-off between accuracy and efficiency, where some algorithms guarantee optimal solutions while others provide faster approximate results.
