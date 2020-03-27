
def solver(currBord):
    stack = [[0, 0, -1]]
    solved = False
    board_coordinates = []
    for i in range(0, 9):
        for j in range(0, 9):
            if(currboard[i, j] == 0)
            board_coordinates.append([i, j])

    while (solved=False):
        backtracking = False
        last_move = stack.pop()
        rnum = last_move[0]
        cnum = last_move[1]
        num = last_move[2] + 1
        for i in range(rnum, 9):
            for j in range(cnum, 9):
                while((checkMove([i, j, num], currBoard) != True) and
                      ([i, j] not in board_coordinates)):
                    if (num > 9):
                        backtrack = True
                        currBoard = reset_move([i, j, num], currBoard)
                        break

                    else:
                        num += 1
                if(backtracking == False and (num != 0)):
                    stack.append([i, j, num])
                    if([i, j] not in board_coordinates):
                        currBoard updateBoard([i, j, num], currBoard)
                else:
                    break
            if(backtracking == True):
                break
        solved = isSolved(currBoard)
