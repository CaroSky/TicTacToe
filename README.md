# Tic-Tac-Toe with AI

This is a Python implementation of the classic Tic-Tac-Toe game with a graphical user interface (GUI) using Tkinter. The game features an AI opponent that uses the minimax algorithm with alpha-beta pruning to make optimal moves.

## Features

- Graphical user interface using Tkinter
- Play against an AI that never loses
- Alternating first moves between human and AI
- Scoreboard to track wins, losses, and ties
- Option to start a new game at any time

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## How to Play

1. The game starts with a 3x3 grid.
2. The human player uses 'X', and the AI uses 'O'.
3. Players take turns placing their symbol in an empty cell.
4. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.
5. If all cells are filled and no player has won, the game is a tie.

## Game Controls

- Click on an empty cell to make your move.
- The "New Game" button starts a new game at any time.
- The scoreboard at the bottom shows the current score.
- A label indicates whose turn it is.

## AI Algorithm

The AI uses the minimax algorithm with alpha-beta pruning to make its decisions. This ensures that the AI always makes the optimal move, making it unbeatable. The best a human player can achieve against this AI is a draw.
