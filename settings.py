import numpy as np
import pygame
import sys
WIDTH = 470
HEIGHT = 550

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW = (192, 192, 192)
GREEN = (127, 255, 212)

# boards
emptyBoard = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Difficulty
difficulty = 40

# Positioning/sizing
grid_position = (10, 90)
cell_size = 50
grid_size = cell_size * 9
timer_position = (190, 60)
sudoku_text_position = (135, 10)

game_font = 'arial'
play_button_text_size = 50
button_text_size = 30
sudoku_text_size = 70
number_text_size = cell_size
