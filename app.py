import pygame
import sys
from settings import *
from buttons import *
from helper_functions import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = None
        self.initial_grid = None
        self.selected = None
        self.selected_indx = None
        # can't initiate mouse_position as None because giving me an error in
        # mouseOnGrid
        self.mouse_position = [0, 0]
        self.number = None
        self.state = 'menu'
        self.move = []
        self.playing_buttons = []
        self.menu_buttons = []
        self.font = pygame.font.SysFont(game_font, number_text_size)
        self.timer_font = pygame.font.SysFont(game_font, button_text_size)
        self.sudoku_font = pygame.font.SysFont(game_font, sudoku_text_size)
        self.button_font = pygame.font.SysFont(game_font, button_text_size)
        self.play_font = pygame.font.SysFont(game_font, play_button_text_size)
        self.difficulty = None
        self.end_time = None
        self.start_time = None
        self.loadButtons()

    def run(self):
        while self.running:
            if self.state == 'menu':
                self.menu_events()
                self.menu_update()
                self.menu_draw()
            if self.state == 'init':
                self.grid = newBoard(emptyBoard, self.difficulty)
                self.initial_grid = self.grid.copy()
                self.state = 'playing'
            if self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            if self.state == 'solving':
                self.solverGame(self.grid)
                self.state = 'solved'
                self.end_time = (pygame.time.get_ticks() //
                                 1000 - self.start_time)
            if self.state == 'solved':
                self.solved_events()
                self.solved_update()
                self.solved_draw()

        pygame.quit()
        sys.exit()
# Solved Functions

    def solved_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # change state to menu if menu button clicked
                if(self.playing_buttons[1].rect.collidepoint(self.mouse_position)):
                    self.state = 'menu'

    def solved_update(self):
        self.mouse_position = pygame.mouse.get_pos()
        for button in self.playing_buttons:
            button.update(self.mouse_position)

    def solved_draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)
        self.printSolved(self.window)
        self.drawEndTime(self.window)
        self.playing_buttons[1].draw(self.window)
        self.drawNumberShadow(self.window)
        self.drawNumbers(self.window)
        pygame.display.update()

# Menu Functions:

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # change state to menu if menu button clicked
                if(self.menu_buttons[3].rect.collidepoint(self.mouse_position)):
                    self.start_time = pygame.time.get_ticks() // 1000
                    self.state = 'init'

                if(self.menu_buttons[0].rect.collidepoint(self.mouse_position)):
                    for button in self.menu_buttons:
                        button.color = SHADOW
                    self.difficulty = 20
                    self.menu_buttons[0].color = GREEN
                if(self.menu_buttons[1].rect.collidepoint(self.mouse_position)):
                    for button in self.menu_buttons:
                        button.color = SHADOW
                    self.difficulty = 40
                    self.menu_buttons[1].color = GREEN
                if(self.menu_buttons[2].rect.collidepoint(self.mouse_position)):
                    for button in self.menu_buttons:
                        button.color = SHADOW
                    self.difficulty = 60
                    self.menu_buttons[2].color = GREEN

    def menu_update(self):
        self.mouse_position = pygame.mouse.get_pos()
        for button in self.menu_buttons:
            button.update(self.mouse_position)

    def menu_draw(self):
        self.window.fill(WHITE)
        self.printSudoku(self.window)
        for button in self.menu_buttons:
            button.draw(self.window)
        pygame.display.update()

# Playing Functions:

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Solve if solve button is clicked
                if(self.playing_buttons[0].rect.collidepoint(self.mouse_position)):
                    self.state = 'solving'

                # change state to menu if menu button clicked
                if(self.playing_buttons[1].rect.collidepoint(self.mouse_position)):
                    self.state = 'menu'
                # set selected if mouse is on grid when clicked
                selected = self.mouseOnGrid()
                self.number = None
                if selected:
                    self.selected = selected
                    self.selected_indx = [self.selected[1], self.selected[0]]
                else:
                    self.selected = None

            if event.type == pygame.KEYDOWN:
                # Check if valid move when enter is pressed
                if event.key == 13:
                    if self.number == None:
                        self.number = 0
                    self.move = [self.selected_indx[0],
                                 self.selected_indx[1], self.number]
                    valid_move = checkMove(self.move, self.grid)
                    if valid_move:
                        self.grid = updateBoard(self.move, self.grid)
                    self.solved = isSolved(self.grid)
                    if self.solved:
                        self.end_time = pygame.time.get_ticks() / 1000
                        self.end_time = (pygame.time.get_ticks() //
                                         1000 - self.start_time)
                        self.state = 'solved'
                # reset position back to zero if delete is pressed
                if event.key == 8:
                    self.move = [self.selected_indx[0],
                                 self.selected_indx[1], self.number]
                    grid = resetMove(self.move, self.grid)
                # number event keys are 49 - 57 instead of 1 - 9 for some reason
                if event.key in [49, 50, 51, 52, 53, 54, 55, 56, 57]:
                    self.number = event.key - 48
                else:
                    self.number = 0

    def playing_update(self):
        self.mouse_position = pygame.mouse.get_pos()
        for button in self.playing_buttons:
            button.update(self.mouse_position)

    def playing_draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)
        self.printSudoku(self.window)
        self.drawTimer(self.window)
        for button in self.playing_buttons:
            button.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected, self.initial_grid)
            if self.number:
                self.drawInputNumbers(
                    self.window, self.selected, self.grid, self.number)
        self.drawNumberShadow(self.window)
        self.drawNumbers(self.window)
        pygame.display.update()

# App Helper Functions:

    def solverGame(self, board):
        empty = findEmpty(board)
        if(not empty):
            return(True)
        else:
            for i in range(1, 10):
                if checkMove([empty[0], empty[1], i], board):
                    board[empty[0]][empty[1]] = i
                    if(self.solverGame(board) == True):
                        return True
                board[empty[0], empty[1]] = 0
        return False

    def drawSelection(self, window, position, board):
        # board is (row, column) but mouse_position returns (column, row)
        if(board[position[1], position[0]] == 0):
            pygame.draw.rect(window, SHADOW, (grid_position[0] + cell_size * position[0],
                                              grid_position[1] + cell_size * position[1], cell_size, cell_size), 2)

    def drawGrid(self, window):
        pygame.draw.rect(
            window, BLACK, (grid_position[0], grid_position[1], WIDTH - 20, HEIGHT - 100), 2)
        for x in range(9):
            if(x % 3 != 0):
                pygame.draw.line(window, BLACK, (grid_position[0] + x * cell_size, grid_position[1]), (
                    grid_position[0] + x * cell_size, grid_position[1] + 450))
            else:
                pygame.draw.line(window, BLACK, (grid_position[0] + x * cell_size, grid_position[1]), (
                    grid_position[0] + x * cell_size, grid_position[1] + 450), 2)

        for x in range(9):
            if(x % 3 != 0):
                pygame.draw.line(window, BLACK, (grid_position[0], grid_position[1] + x * cell_size), (
                    grid_position[0] + 450, grid_position[1] + x * cell_size))
            else:
                pygame.draw.line(window, BLACK, (grid_position[0], grid_position[1] + x * cell_size), (
                    grid_position[0] + 450, grid_position[1] + x * cell_size), 2)

    def drawTimer(self, window):
        currTime = (pygame.time.get_ticks() // 1000 - self.start_time)
        font = self.timer_font.render(
            'Time: ' + str(currTime), False, BLACK)
        window.blit(font, timer_position)

    def drawNumbers(self, window):
        for yindx, row in enumerate(self.grid):
            for xindx, num in enumerate(row):
                if num != 0:
                    pos = [xindx * cell_size + grid_position[0] + 15,
                           yindx * cell_size + grid_position[1] + 10]
                    self.textPrint(window, str(num), pos)

    def drawNumberShadow(self, window):
        for yindx, row in enumerate(self.initial_grid):
            for xindx, num in enumerate(row):
                if num != 0:
                    pos = [xindx * cell_size + grid_position[0] + 15,
                           yindx * cell_size + grid_position[1] + 10]
                    pygame.draw.rect(window, SHADOW, (xindx * cell_size +
                                                      grid_position[0] + 2, yindx * cell_size + grid_position[1] + 2, cell_size - 2, cell_size - 2))

    def drawInputNumbers(self, window, position, board, number):
        position = [position[0] * cell_size + grid_position[0] + 15,
                    position[1] * cell_size + grid_position[1] + 10]
        self.textPrint(window, str(number), position)

        pass

    def mouseOnGrid(self):
        if (self.mouse_position[0] < grid_position[0]) or (self.mouse_position[1] < grid_position[1]):
            return(False)
        if (self.mouse_position[0] > grid_position[0] + grid_size) or (self.mouse_position[1] > grid_position[1] + grid_size):
            return(False)
        # switched mouse_position[0] and mouse_position[1] around becuase it is in relation to the top left corner
        return (((self.mouse_position[0] - grid_position[0]) // cell_size), ((self.mouse_position[1] - grid_position[1]) // cell_size))

    def loadButtons(self):
        # Menu state buttons
        self.menu_buttons.append(
            Button(60, 100, 52, 20, "Easy", self.button_font))
        self.menu_buttons.append(
            Button(185, 100, 82, 20, "Medium", self.button_font))
        self.menu_buttons.append(
            Button(350, 100, 52, 20, "Hard", self.button_font))
        self.menu_buttons.append(
            Button(187, 200, 80, 40, "Play", self.play_font))

        # Playing state buttons
        self.playing_buttons.append(
            Button(390, 60, 60, 20, "Solve", self.button_font))
        self.playing_buttons.append(
            Button(20, 60, 60, 20, "Menu", self.button_font))

    def textPrint(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        window.blit(font, pos)

    def printSudoku(self, window):
        font = self.sudoku_font.render('Sudoku', False, BLACK)
        window.blit(font, sudoku_text_position)

    def printSolved(self, window):
        font = self.sudoku_font.render('Solved!', False, GREEN)
        window.blit(font, sudoku_text_position)

    def printMenu(self, window):
        font = self.sudoku_font.render('Main Menu', False, BLACK)
        window.blit(font, sudoku_text_position)

    def drawEndTime(self, window):
        font = self.timer_font.render(
            'Time: ' + str(self.end_time), False, BLACK)
        window.blit(font, timer_position)
