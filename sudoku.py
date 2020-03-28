from buttons import *
from helper_functions import *
from settings import*
import numpy as np
import pandas as pd
from app import *

testBoard = np.array([
    [5, 0, 5, 0, 5, 0, 5, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
])


def sudoku_solver(board):
    solver(board)
    print('solved')
    print(board)


if __name__ == '__main__':
    app = App()
    app.run()
