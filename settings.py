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

GAME_SETTINGS = {
    # window height
    "height": 500,

    # window width
    "width": 500,
}

PLAYER_SETTINS = {
    "sprite_height": 32,
    "sprite_width": 32,
    "starting_x": 225,
    "starting_y": 300,
    "velocity": 10,
}

PLAYER_SPRITES = {
    "right": pygame.image.load('images/pac-right.bmp'),
    "left": pygame.image.load('images/pac-left.bmp'),
    "up": pygame.image.load('images/pac-up.bmp'),
    "down": pygame.image.load('images/pac-down.bmp'),
}
