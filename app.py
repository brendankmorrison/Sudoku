import pygame
import sys
from settings import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testBoard
        print(self.grid)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)
        pygame.display.update()

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
