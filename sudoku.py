from boards import *
from board_generator import *
import numpy as np
import pandas as pd
from app import *

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


def game(board):
    solved = False
    moves = []
    currBoard = board
    while (solved != True):
        printBoard(currBoard)
        # check if first move
        if(moves == []):
            choice = 1
        else:
            choice = makeChoice()
            choice = int(choice)
            print("Past moves are: ")
            print(moves)
        # make or replace move
        if(choice == 1):  # make move
            currMove = makeMove()
            is_valid = checkMove(currMove, currBoard)
            if(is_valid == True):
                currBoard = updateBoard(currMove, currBoard)
                solved = isSolved(currBoard)
                moves.append(currMove)
            else:
                print("not a valid move.")
        else:  # replace move
            inMoves = False
            # Check if move player wants to replace
            # is in the list of previous moves
            while(inMoves == False):
                print("What move would you like to replace?")
                replace = makeMove()
                if (replace in moves):
                    inMoves = True
                else:
                    print("Not a past move.")
            validReplacement = False
            # Check if replacement player wants to make
            # is a valid replacement
            temp = replace.copy()
            while(validReplacement == False):
                num = input("Enter a replacement number")
                num = int(num)
                currBoard = resetMove(replace.copy(), currBoard)
                moves.remove(temp)
                replace[2] = num
                is_valid = checkMove(replace, currBoard)
                if(is_valid == True):
                    currBoard = updateBoard(replace, currBoard)
                    solved = isSolved(currBoard)
                    moves.append(replace)
                    validReplacement = True
                else:
                    print("not a valid replacement.")
                    currBoard = updateBoard(temp, currBoard)
                    moves.append(temp)
    printBoard(currBoard)
    print("Board is solved!")


def sudoku_solver(board):
    solver(board)
    print('solved')
    print(board)


if __name__ == '__main__':
    board = newBoard(emptyBoard)
    print(board)
    app = App(board)
    app.run()
