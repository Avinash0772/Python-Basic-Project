# Tic Tac Toe Game

A graphical Tic Tac Toe game built with Python's Tkinter library. Play against an AI opponent with score tracking and multiple game rounds.

## Overview

This project provides a user-friendly graphical interface for playing the classic Tic Tac Toe game. You can play against an AI opponent that makes intelligent random moves, with a built-in scoring system to track wins across multiple games.

## Features

- **Graphical User Interface**: Built with Tkinter for easy interaction
- **AI Opponent**: Computer opponent with random move selection
- **Score Tracking**: Keep track of X and O wins across multiple games
- **Win Detection**: Automatic detection of 8 possible winning combinations
- **Draw Detection**: Identifies when the game ends in a tie
- **Game Reset**: Quick restart button to play again
- **Visual Feedback**: Color-coded board with winning combinations highlighted in green
- **Turn Indicator**: Clear display of whose turn it is

## Requirements

- Python 3.x
- Tkinter (usually comes with Python by default)

## How to Run

```bash
python code.py
```

## Game Rules

- Players take turns placing their mark (X or O) on a 3x3 grid
- First player (X) always goes first
- A player wins by getting three of their marks in a row:
  - Horizontally (top, middle, or bottom)
  - Vertically (left, center, or right)
  - Diagonally (both directions)
- If all 9 squares are filled without a winner, the game is a draw

## How to Play

1. Run the program to open the GUI window
2. The board shows a 3x3 grid with 9 empty squares
3. Click on any empty square to place your mark (X)
4. The AI opponent (O) automatically makes its move after your turn
5. The current player's turn is displayed at the top
6. When someone wins or the board is full, a message appears
7. Click the "Restart Game" button to play again
8. The score is updated and displayed

## Game Interface

- **Board**: 9 clickable buttons arranged in a 3x3 grid
- **Turn Display**: Shows whose turn it is
- **Score Display**: Shows current win count for X and O
- **Restart Button**: Resets the board for a new game

## Features Explained

- **Player Marks**: X is displayed in blue, O is displayed in red
- **Winning Squares**: Turn green when a player wins
- **AI Logic**: Computer randomly selects from available squares
- **Message Boxes**: Pop-up notifications for game outcomes

## Author

Avinash0772
