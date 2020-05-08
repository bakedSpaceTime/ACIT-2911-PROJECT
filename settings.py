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

    "tile_side_length": 30,
}

PLAYER_SETTINS = {
    "sprite_height": 32,
    "sprite_width": 32,
    "starting_x": 585,
    "starting_y": 690,
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
        "starting_y": 180,
        "velocity": 8,
    },
    {
        "starting_x": 1270,
        "starting_y": 570,
        "velocity": 12,
    },
]

VIRUS_SPRITES = {
    "right": pygame.image.load(path_join('images','pac-right.bmp')),
    "left": pygame.image.load(path_join('images','pac-left.bmp')),
    "up": pygame.image.load(path_join('images','pac-up.bmp')),
    "down": pygame.image.load(path_join('images','pac-down.bmp')),
}
# car sprite from https://www.pinterest.ca/pin/233624299398167646/
OTHER_SPRITES = {
    "toilet_paper": pygame.image.load(path_join('images','Toilet Paper.png')),
    "shelf_front": pygame.image.load(path_join('images','Shelf', 'Front.png')),
    "shelf_side": pygame.image.load(path_join('images', 'Shelf', 'Sides.png')),
    "wall": pygame.image.load(path_join('images','Shelf', 'wall.png')),
    "hand_sanitizer": pygame.image.load(path_join('images','sanitizer-sprite.png')),
    "railing_front": pygame.image.load(path_join('images', 'Shelf', 'railing_front2.png')),
    "railing_side": pygame.image.load(path_join('images', 'Shelf', 'railing_side3.png')),
    "tree": pygame.image.load(path_join('images', 'tree.png')),
    "car1": pygame.image.load(path_join('images', 'cars', 'car1.png')),
    "car2": pygame.image.load(path_join('images', 'cars', 'car2.png')),
    "car3": pygame.image.load(path_join('images', 'cars', 'car3.png')),
}

BACKGROUND = pygame.image.load(path_join('images','background.png'))

WALL_LIST_1ST_FLOOR = {
    "loot":
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W=================W====================W",
        "W==S===S===S======W=##################=W",
        "W==S=S=SHS=S=S====W====================W",
        "W==S=S=S=S=S=S=========================W",
        "W=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW==W",
        "W==================================HW==W",
        "W==################=======##########W==W",
        "W===================================W==W",
        "W===#############=======WWWWWWWWWWWWW==W",
        "W=======================S===S=H=S===W==W",
        "W=WWWWWWWWWWWWWWWWW=====S=#=S=#=S=#=W==W",
        "W=======================S===S===S===W==W",
        "W===#############======================W",
        "W=========================#########====W",
        "W=WWWWWWWWWWWWWWWWW====================W",
        "W=======================S===S===S===S==W",
        "W===#############=======S=#=S=#=S=#=S==W",
        "W=======================S===S=H=S===S==W",
        "W=WWWWWWWWWWWWWWWW====WWWWWWWWWWWWWWWW=W",
        "W======================================W",
        "W=================W==W=================W",
        "WH================W==W=================W",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
    "virus":
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W+l=============l+W+=================l+W",
        "Wl=S===S===S=====lWl##################lW",
        "W==S=S=S=S=S=S===lW===================lW",
        "Wl=S=S=S=S=S=S===+l+l================l+W",
        "W+WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=lW",
        "W+==================================W==W",
        "Wl=################=======##########W==W",
        "W===================================W==W",
        "W===#############=======WWWWWWWWWWWWW==W",
        "W=======================S===S===S===W==W",
        "W=WWWWWWWWWWWWWWWWW=====S=#=S=#=S=#=W==W",
        "W=======================S===S===S===W==W",
        "W===#############======================W",
        "W=========================#########====W",
        "W=WWWWWWWWWWWWWWWWW====================W",
        "W=======================S===S===S===S==W",
        "W===#############=======S=#=S=#=S=#=S==W",
        "Wl======================S===S===S===S=lW",
        "W+WWWWWWWWWWWWWWWW+ll+WWWWWWWWWWWWWWWW+W",
        "W+l=====l+l=====l+l==l+l=====l+l=====l+W",
        "Wl=======l=======lW==Wl=======l=======lW",
        "W+l======+======l+W==W+l======+======l+W",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
}

WALL_LIST_PARKING_LOT = [
    "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
    "TC==========R=======R==========HR======T",
    "T=C==========CC===============C=C======T",
    "T===RRRRRRR======RRR=RRRRRRRRRr====RRRRT",
    "T==C======C==C=====C==========r========T",
    "T====r=Rr====C=====C=========CrC=======T",
    "T==r=r=Hr==RRRRR==CC====RRRR==r==rRRRRRT",
    "T==r=rR=r====C============C===r==r=C===T",
    "T==r======C=======C==RRRRRRR==r==r===C=T",
    "T==r======R===C===RRRR=====C==r=====C==T",
    "T=====CC==RRRR==========R==========R===T",
    "T==C=========r=====C===RCR==Cr==r==RRRRT",
    "T==RRRRRRRRRRR===C======R====r==r======T",
    "T===============CCCC==C===C==r==r=rRRR=T",
    "T========C=C==C===C===RRRRR==r====r====T",
    "T==rRRRRRR==RR==C============rC===rRR==T",
    "T==rH=r==C==RR==C==RRRRRR==RRRRR====C==T",
    "T==r==r====C==C====R=============RR====T",
    "T==r===============C==C=====C==rRRRRrRRT",
    "T==rRRRRRC===RRr======rRRRRRR==r====r==T",
    "T==r==========Cr==C===r========r=C=Hr==T",
    "T=====RRR===C==r===C==r=C=CRC==rRR=CrC=T",
    "T====C======C=====C=====C==============T",
    "TTTTTTTTTTTTTTTTTTT==TTTTTTTTTTTTTTTTTTT",
]

WALL_LIST = [
    # "#############",
    # "#+#+#+#+====#",
    # "#l#l#l#l====#",
    # "#=#=#=#=====#",
    # "#=#=#=#=====#",
    # "#=#=#=#=====#",
    # "#=#=#=#=====#",
    # "#l#l#l#l====#",
    # "#+l+l+l===l+#",
    # "#############",
    "########################################",
    "#+l==================================l+#",
    "#l=###################################l#",
    "#+l================================l+#=#",
    "#l=###################################=#",
    "#+l================================l+#=#",
    "#l=###################################=#",
    "#+l================================l+#=#",
    "#l=###################################=#",
    "#+l================================l+#=#",
    "#l=###################################l#",
    "#+l==================================l+#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=l#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#==#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#==#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#==#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#==#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#==#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#==#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#==#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#==#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=l#",
    "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=+#",
    "########################################",
]
