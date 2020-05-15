"""
Pandemic Run
Course: ACIT 2911, Agile Development
Authors:
- Jaskaran Saini, A01055847
- Jeffery Law, A00864331
- Ming Yen Hsieh, A01170219
- Tushya Iyer, A01023434
- Shivar Pillay, A01079978
- Shivam Patel, A01185250
"""

import pygame
vec = pygame.math.Vector2


class Button():
    def __init__(self, x, y, width, height, text, bg_color, font_color, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.bg_color = bg_color
        self.font_color = font_color
        self.font = pygame.font.Font('freesansbold.ttf', font_size)

    def draw(self, window):
        button = pygame.draw.rect(window, self.bg_color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, True, self.font_color)
        window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def clicked(self, mx, my):
        if self.x < mx < self.x + self.width:
            if self.y < my < self.y + self.height:
                return True
        return False
