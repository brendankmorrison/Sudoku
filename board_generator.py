from helper_functions import *

def newBoard(board):
    newBoard = board.copy()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in nums:
        x = np.random.randint(0, 9, 1)
        y = np.random.randint(0, 9, 1)
        if(newBoard[x, y] == 0):
            newBoard[x, y] = i
    solver(newBoard)
    for i in range(0, 40):
        x = np.random.randint(0, 9, 1)
        y = np.random.randint(0, 9, 1)
        if(newBoard[x, y] != 0):
            newBoard[x, y] = 0
    return newBoard
