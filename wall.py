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
from math import ceil
from os.path import join as path_join
from settings import OTHER_SPRITES


class Obstacle(pygame.sprite.Sprite):
    """ Obstacle Class """
    def __init__(self, x, y, type = 'wall'):
        """ Obstacle Constructor """
        super().__init__()
        self.image = OTHER_SPRITES[type].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
