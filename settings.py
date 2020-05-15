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
    "height": 780,

    # window width
    "width": 1200,

    "tile_side_length": 30,
}

COLOURS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "blue": (25, 25, 166),
    "yellow": (255, 255, 0),
    "red": (255, 0, 0),
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
        "velocity": 30#8,
    },
    {
        "starting_x": 1270,
        "starting_y": 570,
        "velocity": 30#12,
    },
    {
        "starting_x": 510,
        "starting_y": 360,
        "velocity": 30#10,
    },
]

VIRUS_SPRITES = {
    "right": pygame.image.load(path_join('images','Virus.png')),
    "left": pygame.image.load(path_join('images','Virus.png')),
    "up": pygame.image.load(path_join('images','Virus.png')),
    "down": pygame.image.load(path_join('images','Virus.png')),
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
    "tree": pygame.image.load(path_join('images', 'Tree.png')),
    "car1": pygame.image.load(path_join('images', 'cars', 'car1.png')),
    "car2": pygame.image.load(path_join('images', 'cars', 'car2.png')),
    "car3": pygame.image.load(path_join('images', 'cars', 'car3.png')),
    "paper_icon": pygame.image.load(path_join('images', 'toilet_big.png')),
    "sanitizer_icon": pygame.image.load(path_join('images', 'sanitizer_icon.png')),
}

BACKGROUND = pygame.image.load(path_join('images','background.png'))

WALL_LIST_1ST_FLOOR = {
    "loot":
    [   "                                        ",
        "                                        ",
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
        "                                        ",
        "                                        ",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W+ll+l+l+l+l+l+ll+W+l=======l+l======l+W",
        "Wl=Sl+lSl+lSl+l==lWl##################lW",
        "W==SlSlSlSlSlSl==lWl==================lW",
        "W==S+S+S+S+S+S+ll+l+l=======l+l======l+W",
        "WlWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=lW",
        "W+l======l+l======l+l+l+l===l+l===l+W==W",
        "Wl=################l=l=l==##########W=lW",
        "W+l======l+l======l+l+l+l===l+l===l+W=+W",
        "Wl==#############==l=l=lWWWWWWWWWWWWW=lW",
        "W+l======l+l======l+l+l+S+l+S+l+S+l+W==W",
        "WlWWWWWWWWWWWWWWWWWl=l=lSl#lSl#lSl#lW==W",
        "W+l======l+l======l+l+=lSl+lSl+lSl+lW=lW",
        "Wl==#############==l=l=+l+l+l+l+l+l+ll+W",
        "W+l======l+l======l+l+ll+l#########l==lW",
        "WlWWWWWWWWWWWWWWWWWl+l=+l+l+l+l+l+l+ll+W",
        "W+l======l+l======l+l+=lSl+lSl+lSl+lS=lW",
        "Wl==#############==l+l=lSl#lSl#lSl#lS==W",
        "W+l======l+l======l+l+l+S+l+S+l+S+l+S==W",
        "WlWWWWWWWWWWWWWWWW=l=lWWWWWWWWWWWWWWWWlW",
        "W+l=============l+l+l+l======l+l=====l+W",
        "Wl===============lW==W========l=======lW",
        "W+l=============l+W==W+l=====l+l=====l+W",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
}

WALL_LIST_2ND_FLOOR = {
    "loot":
    [
        "                                        ",
        "                                        ",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W==============S==========S====WWWWW===W",
        "W==WWWWWWW=====S=#S###S#==S============W",
        "W==WH==========S==S=H=S===S==S===S==S==W",
        "W==W===========S==S===S===S==S===S==S==W",
        "W==WWWWW=W=====S==S=S=S===S==S===S==S==W",
        "W======================================W",
        "W===========S##====########==##==#####=W",
        "W#########==S==========================W",
        "W===========#######===####S============W",
        "W=============S===========S==###=###=##W",
        "W==###====S###==########==S============W",
        "W=========S============================W",
        "W=========================S==####==###=W",
        "W=######==#=##S==#######===============W",
        "W=============S========================W",
        "W=========##=######=####===###########SW",
        "W#######==============================SW",
        "W============S==S==S==S==S============SW",
        "W==###===S===S==S==S==S==SS==S==S==S==SW",
        "W===H====S===S==S=====S==SS==S==S==S==SW",
        "W=#####==S===S==S=W==WS==SS==S==S==S==SW",
        "W=================W==W===S===========HSW",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
    "virus":
    [
        "                                        ",
        "                                        ",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W+l==l+l==l+ll+S+l=l+l==l+S+ll+WWWWW===W",
        "Wl=WWWWWWW=l==lSl#S###S#=lSl==l=+ll+ll+W",
        "W==W+l====l+===S==S+l+S+l+S==S==lS=lS=lW",
        "W==W===========S==Sl=lSl=lS==S===S==S==W",
        "Wl=WWWWW=W=l==lSl=SlSlSl=lS==Sl=lS=lS=lW",
        "W+l=======l+ll+l+ll+l+l+l+l==l+l+ll+ll+W",
        "W==========lS##=l==########l=##=l#####lW",
        "W#########==S+ll+l=l+l====l+l========l+W",
        "W+l====l+==l#######=l=####Sl===========W",
        "Wl====+ll+l+l+S+l==l+l=l+=S==###=###=##W",
        "W==###l===S###=l########l=Sl====l======W",
        "Wl====l==lS+l==l========l=l+l==l+l+l+l+W",
        "W+l==l+ll+l===l+l======l+=Sl=####=l###lW",
        "Wl######ll#=##Sl=#######l==l======l===lW",
        "Wl======+l=l+=S+l=l+l==l+ll+l====l+l=l+W",
        "W+l=====l+##l######l####l==###########SW",
        "W#######l=+l=l+ll+l+l+ll+ll+ll+ll+l=l+SW",
        "W+l====l+lll+Sl=Sl=S=lS=lS=l==l==l===lSW",
        "Wl=###==lS==lS==Sl=S=lS==SS==S==S==S==SW",
        "W+l====l+S===S==S+l=l+S==SS==S==S==S==SW",
        "Wl#####=lSl==Sl=SlW==WS=lSSl=Sl=Sl=S=lSW",
        "W+l===l+ll+l+l+ll+W==W==+S=+ll+ll+l=l+SW",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
}

WALL_LIST_PARKING_LOT = {
    "loot":
        [
            "                                        ",
            "                                        ",
            "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
            "TC==========R==================HR======T",
            "T============CC===============C=C======T",
            "T===RRRR=RR======RRR=RRRRRRRRRr====RRRRT",
            "T==C======C==C=====C==========r========T",
            "T====r=R=====C=====C=========CrC=======T",
            "T====r=Hr====R=R==CC====RRRR=====rRRRRRT",
            "T==r==R=r====C============C===r==r=====T",
            "T==r======C=======C==RRRR=RR==r==r===C=T",
            "T==r======R=======RRRR=====C==r=====C==T",
            "T=====CC==RRR===========R==========R===T",
            "T==C=========r=========RCR==Cr==r==RRRRT",
            "T==RR=RRRRRRRR===C===========r==r======T",
            "T================CC===C===C==r==r=rRRR=T",
            "T========C=C==C===C====RRRR==r====r====T",
            "T==rRRRRRR==RR==C============rC===r=R==T",
            "T==rH=r==C==RR==C==RR==RR===RRRR====C==T",
            "T==r==r====C==C====R=============RR====T",
            "T==r========================C==rRRRRrRRT",
            "T==rRRRRRC===RRr=======RRRRRR==r====r==T",
            "T==r==========Cr==C===r========r=C=Hr==T",
            "T=====RRR===C==r===C==r=C=CRC==rRR=CrC=T",
            "T====C======C=====C=====C==============T",
            "TTTTTTTTTTTTTTTTTTT==TTTTTTTTTTTTTTTTTTT",

            # Old map
            # "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
            # "TC==========R=======R==========HR======T",
            # "T=C==========CC===============C=C======T",
            # "T===RRRRRRR======RRR=RRRRRRRRRr====RRRRT",
            # "T==C======C==C=====C==========r========T",
            # "T====r=Rr====C=====C=========CrC=======T",
            # "T==r=r=Hr==RRRRR==CC====RRRR==r==rRRRRRT",
            # "T==r=rR=r====C============C===r==r=C===T",
            # "T==r======C=======C==RRRRRRR==r==r===C=T",
            # "T==r======R===C===RRRR=====C==r=====C==T",
            # "T=====CC==RRRR==========R==========R===T",
            # "T==C=========r=====C===RCR==Cr==r==RRRRT",
            # "T==RRRRRRRRRRR===C======R====r==r======T",
            # "T===============CCCC==C===C==r==r=rRRR=T",
            # "T========C=C==C===C===RRRRR==r====r====T",
            # "T==rRRRRRR==RR==C============rC===rRR==T",
            # "T==rH=r==C==RR==C==RRRRRR==RRRRR====C==T",
            # "T==r==r====C==C====R=============RR====T",
            # "T==r===============C==C=====C==rRRRRrRRT",
            # "T==rRRRRRC===RRr======rRRRRRR==r====r==T",
            # "T==r==========Cr==C===r========r=C=Hr==T",
            # "T=====RRR===C==r===C==r=C=CRC==rRR=CrC=T",
            # "T====C======C=====C=====C==============T",
            # "TTTTTTTTTTTTTTTTTTT==TTTTTTTTTTTTTTTTTTT",
        ],
    "virus":
        [
            "                                        ",
            "                                        ",
            "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
            "TC+l=l+l+ll+R+ll+l=l+l==l+l==l+HR======T",
            "T=ll====l==l=CC=l===l=========C=C======T",
            "T+l+RRRR+RR+ll+l+RRRlRRRRRRRRRr====RRRRT",
            "TllC====l+Cl=Cl=ll+C+l======l+r========T",
            "Tl+==r=R+ll+=C=====Cl========CrC=======T",
            "T+ll+r=Hr+ll+RlR=+CCl===RRRR+l=l+rRRRRRT",
            "Tl=rl+R=rl=llC=+ll=l+l==l+C=l=r=lr+l=l+T",
            "T==r+l==l+C+l+ll+lC==RRRRlRR==r==rl==ClT",
            "Tl=rll+l=lR=+l+ll+RRRR+l+l+Cl=r=l=l=C+lT",
            "T+lll+CC=lRRR+l+ll+ll+l+R+ll+l+l+l+R+l+T",
            "Tl=C+l==l+ll+r+l++l+=llRCR++Crl=r=lRRRRT",
            "Tl=RR+RRRRRRRRl=lC+l+l+l+l+l+r==r=+l=l+T",
            "T+l==l=l+l+l=l+l+CC===C+l+C+lrl=r=rRRRlT",
            "Tl+ll+ll+ClC==C+l+Cl+l+RRRR=lr+l+=r+ll+T",
            "T=lrRRRRRR==RR=lC+l+l+l+l+ll+rC=l=rlR=lT",
            "T==rH+r+=C==RR==Cl=RR=+RRl=+RRRRl==lC=lT",
            "T==r+lrl==lC==Cl=l=R+ll=l+ll=l+l+RR+ll+T",
            "T=lr=+l+ll+l==l+l+l=l+l===l+C=lrRRRRrRRT",
            "T=+rRRRRRCl==RRr=l===l+RRRRRR=lr====r=+T",
            "T==r+l===l+ll+Cr==C===r+l====l+r=C=Hr=lT",
            "Tl==l=RRR=l=Cl=r=l=C=lrlC=CRC=lrRR=CrClT",
            "T+ll+C+l=l+=C+l=l+C+l+l+C+l==l+l=====l+T",
            "TTTTTTTTTTTTTTTTTTT==TTTTTTTTTTTTTTTTTTT",
        ],
}
