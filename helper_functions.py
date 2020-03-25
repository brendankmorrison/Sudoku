import numpy as np


def checkMove(currMove, currBoard):
    isValid = True
    # check if move has already been made
    if(currBoard[currMove[0]][currMove[1]] != 0):
        isValid = False
    # Check if row has no conflict
    if(currMove[2] in currBoard[currMove[0]]):
        isValid = False
    # Check if column has no conflicts
    if(currMove[2] in currBoard[:, currMove[1]]):
        isValid = False
    # Check if square has no conflicts
    row = 0
    if(currMove[0] < 3):
        row = range(0, 3)
    elif(currMove[0] < 6):
        row = range(3, 6)
    else:
        row = range(6, 9)
    if(currMove[1] < 3):
        square = currBoard[row, 0: 3]
    elif(currMove[1] < 6):
        square = currBoard[row, 3: 6]
    else:
        square = currBoard[row, 6: 9]
    if(currMove[2] in square):
        isValid = False
    return(isValid)


def updateBoard(currMove, currBoard):
    currBoard[currMove[0]][currMove[1]] = currMove[2]
    return(currBoard)


def makeMove():
    valid_input = False
    while(valid_input == False):
        row, col, num = input(
            "Enter row index, column index, and number:").split()
        row = abs(int(row))
        col = abs(int(col))
        num = abs(int(num))
        currMove = [row, col, num]
        if((currMove[0] < 9) and (currMove[1] < 9) and (currMove[2] < 10)):
            valid_input = True
        else:
            print("Not a valid input.")
    return currMove


def printBoard(currBoard):
    # Prints the board to the console

    # prints rows but before row index 3 and
    # row index 6 print a horizontal line
    count_row = 0
    for i in range(0, 9):
        count_col = 0
        if ((count_row == 3) or (count_row == 6)):
            print("-------------------------")

        # prints elements of row but before col index 3 and
        # col index 6 print a vertical line
        for j in range(0, 9):
            if ((count_col == 3) or (count_col == 6)):
                print(" | ", end=' ')
            print(currBoard[i][j], end=' ')
            count_col += 1

        count_row += 1
        print('')


def makeChoice():
    valid_input = False
    while(valid_input == False):
        print("Do you want to make a move or replace a move?")
        choice = input("make = 1, replace = 0")
        choice = int(choice)
        if((choice == 1) or (choice == 0)):
            valid_input = True
        else:
            print("not a valid choice.")
    return choice


def isSolved(currBoard):
    solved = True
    for row in currBoard:
        if(0 in row):
            solved = False
    return(solved)


def resetMove(temp, currBoard):
    setZero = temp
    setZero[2] = 0
    currBoard = updateBoard(setZero, currBoard)
    return(currBoard)


def chooseBoard(boards):
    valid_input = False
    while(valid_input == False):
        boardChoice = input("Choose board: ")
        boardChoice = int(boardChoice)
        if(boardChoice in range(0, len(boards))):
            board = boards[boardChoice]
            valid_input = True
        else:
            print('Not a valid board name')
        return(board)
