import pygame
import sys
from settings import *
from buttons import *


class App:
    def __init__(self, board):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = board
        self.selected = None
        self.mouse_position = None
        self.state = 'playing'
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
#            if event.type == pygame.MOUSEBUTTONDOWN:
#                sel = self.mouseOnGrid(self.mouse_position)
#                if sel:
#                    self.selected = sel
#                else:
#                    self.selected = None

    def playing_update(self):
        pass
#        self.mouse_position = pygame.mouse.get_pos()
#        for button in self.playing_buttons:
#            button.update(self.mouse_position)

    def playing_draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)

        for button in self.playing_buttons:
            button.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected, self.board)

        self.drawNumbers(self.window)
        pygame.display.update()


# App Helper Functions

#    def drawSelection(self, window, position, board):
#        if(board[position[0], position[1]] == 0):
#            pygame.draw.rect(window, SHADOW, (grid_position[0] + cell_size * position[0],
#                                              grid_position[1] + cell_size * position[1], cell_size, cell_size), 2)

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

    def drawNumbers(self, window):
        for yindx, row in enumerate(self.grid):
            for xindx, num in enumerate(row):
                if num != 0:
                    pos = [xindx * cell_size + grid_position[0] + 15,
                           yindx * cell_size + grid_position[1] + 10]
                    pygame.draw.rect(window, SHADOW, (xindx * cell_size +
                                                      grid_position[0] + 2, yindx * cell_size + grid_position[1] + 2, cell_size - 2, cell_size - 2))
                    self.textPrint(window, str(num), pos)

#    def mouseOnGrid(self, mouse_position):
#        if (self.mouse_position[0] < grid_position[0]) or (self.mouse_position[1] < grid_position[1]):
#            return(False)
#        if (self.mouse_position[0] > grid_position[0] + grid_size) or (self.mouse_position[1] > grid_position[1] + grid_size):
#            return(False)
#        return ((self.mouse_position[0] - grid_position[0]) // cell_size, (self.mouse_position[1] - grid_position[1]) // cell_size)

    def loadButtons(self):
        self.playing_buttons.append(Button(20, 40, 100, 40))

    def textPrint(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        window.blit(font, pos)
