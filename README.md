# AI Search and Knowledge-Based Systems – Assignment

## Overview

This project focuses on implementing and understanding different AI techniques used for problem solving and decision-making. It includes game search algorithms, a travel planner design using knowledge bases, and basic concepts of probabilistic reasoning.

---

## 1. Game Search Algorithms

In this part, different AI search algorithms were implemented using a Tic-Tac-Toe game:

* **Minimax Algorithm**
* **Alpha-Beta Pruning**
* **Heuristic Alpha-Beta**
* **Monte Carlo Tree Search (MCTS)**

### Description

* **Minimax** checks all possible moves and chooses the best one assuming both players play optimally.
* **Alpha-Beta Pruning** improves Minimax by skipping unnecessary branches, making it faster.
* **Heuristic Alpha-Beta** limits the depth of the search and uses a heuristic to evaluate positions.
* **MCTS** uses random simulations to decide the best move instead of checking everything.

### Test Cases

Three different test cases were used to check correctness:

* Winning scenario
* Blocking scenario
* Empty board

### Observations

* Alpha-Beta is noticeably faster than Minimax
* Heuristic approach helps when full search is not possible
* MCTS gives good results but can vary slightly due to randomness

---

## 2. AI-Based Travel Planner (Design)

In this section, an AI-based travel planner was designed. The goal was to generate personalized travel plans using existing knowledge bases.

### Features

* Takes user input such as budget, location, and preferences
* Uses knowledge bases for tourist places and food recommendations
* Generates a simple day-wise travel plan
* Provides an approximate cost estimate

### Architecture

User Input → Preference Analyzer → Knowledge Base → AI Planner → Output

---

## 3. Knowledge Graphs

Knowledge Graphs are used to represent data in terms of entities and their relationships.

### Key Concepts

* Nodes represent entities
* Edges represent relationships
* Data is stored in the form of triples (Subject → Predicate → Object)

### Tools Used

* Neo4j
* Protégé
* RDF
* SPARQL

---

## 4. Bayesian Networks

Bayesian Networks are used to model uncertain situations using probability.

### Concepts

* Nodes represent variables
* Edges represent dependencies
* Uses Conditional Probability Tables (CPT)

### Tools Used

* pgmpy
* GeNIe
* Netica

### Example

A simple example was used:

* Fever -> Flu
* Cough -> Flu

This shows how different symptoms can influence the probability of having a disease.

---

## Conclusion

This assignment helped in understanding how different AI techniques work in practice. It shows how algorithms, knowledge representation, and probabilistic models can be used together to solve real-world problems. It also highlights the trade-off between accuracy and efficiency in different approaches.
