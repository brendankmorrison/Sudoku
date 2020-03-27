import numpy as np
import pygame
import sys
WIDTH = 470
HEIGHT = 550

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW = (192, 192, 192)

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
timer_position = (10, 10)
