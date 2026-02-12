# Rock Paper Scissors Game

A classic Rock, Paper, Scissors game implementation in Python where players compete against the computer in a best-of-5 series.

## Overview

This is an interactive command-line game where you play Rock, Paper, Scissors against the computer. The game runs for 5 rounds and keeps track of the score to determine the overall winner.

## Features

- **Interactive Gameplay**: Enter your choice (Rock, Paper, or Scissor)
- **Computer Opponent**: Computer makes random choices
- **Score Tracking**: Keeps track of wins, losses, and draws
- **Best of 5 Rounds**: Play 5 rounds to determine the winner
- **Replay Option**: Play multiple games in the same session
- **Input Validation**: Ensures valid input from the user

## Requirements

- Python 3.x
- No external dependencies required

## How to Run

```bash
python code.py
```

## Game Rules

- **Rock** beats Scissor
- **Paper** beats Rock
- **Scissor** beats Paper
- Identical choices result in a Tie

## How to Play

1. Run the program
2. When prompted, enter one of: `Rock`, `Paper`, or `Scissor`
3. The program displays both your choice and computer's choice
4. The round winner is announced
5. Score is updated and displayed
6. After 5 rounds, the overall game winner is declared
7. Choose to play again or exit

## Example Gameplay

```
Welcome to Rock Paper Scissors Game
------ Best of 5 Rounds ------

Round 1
Enter Rock, Paper or Scissor: Rock
You chose: Rock
Computer chose: Scissor
You Win this round!
Score ➝ You: 1 | Computer: 0
```

## Output Information

- **Current Round**: Displayed at the start of each round
- **User and Computer Choices**: Both choices are shown
- **Round Result**: Indicates who won the round
- **Live Score**: Shows current score after each round
- **Final Result**: Announces the overall game winner

## Author

Avinash0772
