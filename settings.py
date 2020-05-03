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
from os.path import join as path_join

GAME_SETTINGS = {
    # window height
    "height": 500,

    # window width
    "width": 500,
}

PLAYER_SETTINS = {
    "sprite_height": 32,
    "sprite_width": 32,
    "starting_x": 450,
    "starting_y": 450,
    "velocity": 10,
}

PLAYER_SPRITES = {
    "right": pygame.image.load(path_join('images','Character', 'Right', 'Right Running 1.png')),
    "left": pygame.image.load(path_join('images','Character', 'Left', 'Left Running 1.png')),
    "up": pygame.image.load(path_join('images','Character', 'Backward', 'Backward Running 1.png')),
    "down": pygame.image.load(path_join('images','Character', 'Forward', 'Forward Running 1.png')),
    "standing_down": pygame.image.load(path_join('images','Character', 'Forward', 'Standing Forward.png'))
}

OTHER_SPRITES = {
    "toilet_paper": pygame.image.load(path_join('images','Toilet Paper.png')),
    "shelf_front": pygame.image.load(path_join('images','Shelf', 'Front.png'))
}

BACKGROUND = pygame.image.load(path_join('images','background.png'))
