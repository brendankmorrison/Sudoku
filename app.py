import pygame
import sys
from settings import *
from buttons import *
from helper_functions import *


class App:
    def __init__(self, board):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = board
        self.initial_grid = board.copy()
        self.selected = None
        self.selected_indx = None
        # can't initiate mouse_position as None because giving me an error in
        # mouseOnGrid
        self.mouse_position = [0, 0]
        self.number = None
        self.state = 'playing'
        self.move = []
        self.playing_buttons = []
        self.menu_buttons = []
        self.end_buttons = []
        self.font = pygame.font.SysFont('times', cell_size)
        self.loadButtons()

    def run(self):
        while self.running:
            if self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            if self.state == 'solve':
                pass

        pygame.quit()
        sys.exit()

# Playing Functions

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                    self.move = [self.selected_indx[0],
                                 self.selected_indx[1], self.number]
                    valid_move = checkMove(self.move, self.grid)
                    if valid_move:
                        self.grid = updateBoard(self.move, self.grid)
                    self.solved = isSolved(self.grid)
                    print(self.solved)
                    if self.solved:
                        self.running = False
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


# App Helper Functions

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
        time_passed = (pygame.time.get_ticks()) // 1000
        self.textPrint(window, str(time_passed), timer_position)

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
        self.playing_buttons.append(Button(20, 40, 100, 40))

    def textPrint(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        window.blit(font, pos)
