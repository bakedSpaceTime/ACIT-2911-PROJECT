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
    "height": 720,

    # window width
    "width": 1200,
}

PLAYER_SETTINS = {
    "sprite_height": 32,
    "sprite_width": 32,
    "starting_x": 450,
    "starting_y": 450,
    "velocity": 10,
    "lives": 10,
    "boosted_duration": 5,
    "invincible_duration": 2,
}

PLAYER_SPRITES = {
    "right": pygame.image.load(path_join('images','Character', 'Right', 'Right Running 1.png')),
    "left": pygame.image.load(path_join('images','Character', 'Left', 'Left Running 1.png')),
    "up": pygame.image.load(path_join('images','Character', 'Backward', 'Backward Running 1.png')),
    "down": pygame.image.load(path_join('images','Character', 'Forward', 'Forward Running 1.png')),
    "standing_down": pygame.image.load(path_join('images','Character', 'Forward', 'Standing Forward.png'))
}

VIRUS_SETTINS = [
    {
        "starting_x": 30,
        "starting_y": 150,
        "velocity": 12,
    },
    {
        "starting_x": 138,
        "starting_y": 90,
        "velocity": 10,
    },
]

VIRUS_SPRITES = {
    "right": pygame.image.load(path_join('images','pac-right.bmp')),
    "left": pygame.image.load(path_join('images','pac-left.bmp')),
    "up": pygame.image.load(path_join('images','pac-up.bmp')),
    "down": pygame.image.load(path_join('images','pac-down.bmp')),
}

OTHER_SPRITES = {
    "toilet_paper": pygame.image.load(path_join('images','Toilet Paper.png')),
    "shelf_front": pygame.image.load(path_join('images','Shelf', 'Front.png')),
    "hand_sanitizer": pygame.image.load(path_join('images','sanitizer-sprite.png'))
}

BACKGROUND = pygame.image.load(path_join('images','background.png'))

WALL_LIST = [
    "########################################",
    "#======================================#",
    "#=#j######=============================#",
    "#=#======#=============================#",
    "#=#j#j##===============================#",
    "#=#j##j#===============================#",
    "#=#====================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "#======================================#",
    "########################################",
]
