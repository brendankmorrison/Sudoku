import pygame
from settings import *


class Button:
    def __init__(self, xpos, ypos, width, height, text, font, color=SHADOW, highlighted_color=BLACK, function=None, params=None):
        self.image = pygame.Surface((width, height))
        self.position = (xpos, ypos)
        self.text_position = (xpos + 3, ypos)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.text = text
        self.color = color
        self.highlighted_color = highlighted_color
        self.function = function
        self.params = params
        self.highlighted = False
        self.font = font
        #self.font = pygame.font.SysFont('times', button_text_size)

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
        font = self.font.render(self.text, False, WHITE)
        window.blit(self.image, self.position)
        window.blit(font, self.text_position)
