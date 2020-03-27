import pygame
from settings import *


class Button:
    def __init__(self, xpos, ypos, width, height, text=None, color=SHADOW, highlighted_color=BLACK, function=None, params=None):
        self.image = pygame.Surface((width, height))
        self.position = (xpos, ypos)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.text = text
        self.color = color
        self.highlighted_color = highlighted_color
        self.function = function
        self.params = params
        self.highlighted = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        if self.highlighted:
            self.image.fill(self.highlighted_color)
        else:
            self.image.fill(self.color)

        window.blit(self.image, self.position)
