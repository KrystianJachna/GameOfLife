# Game of Life in Pygame

A simple implementation of Conway's Game of Life using Pygame.

## How to Play

- Run the script by executing `python main.py` in your terminal.
- Press `SPACE` to start/pause the simulation.
- Press `C` to clear the board.
- Press `R` to populate the board with random cells.
- Click on a cell to toggle its state.

## Rules

The Game of Life follows these rules:

1. **Underpopulation**: A live cell with fewer than two live neighbors dies.
2. **Survival**: A live cell with two or three live neighbors survives.
3. **Overpopulation**: A live cell with more than three live neighbors dies.
4. **Reproduction**: A dead cell with exactly three live neighbors becomes alive.

## Controls

- **SPACE**: Start/Pause simulation
- **C**: Clear the board
- **R**: Populate the board with random cells
- **Mouse Click**: Toggle cell state

## Dependencies

- Python 3.x
- Pygame
- NumPy

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install Pygame by running `pip install pygame`.
3. Install NumPy by running `pip install numpy`.

## Customize

Feel free to modify the script to create your own initial board configurations or add new features.

## Author

Krystian Jachna

