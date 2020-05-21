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

    # Lenght of a standard tile
    "tile_side_length": 30,
}

""" RGB Colour Constants """
COLOURS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "blue": (25, 25, 166),
    "yellow": (255, 255, 0),
    "red": (255, 0, 0),
}

""" Player settings to control attributes rather than hard coding in the constructor """
PLAYER_SETTINS = {
    "sprite_height": 32,
    "sprite_width": 32,
    "starting_x": 585,
    "starting_y": 740,
    "velocity": 8,
    "lives": 10,
    "boosted_duration": 5,
    "invincible_duration": 2,
}

""" Player sprites for easy access to each sprite """
PLAYER_SPRITES = {
    "right_standing": pygame.image.load(path_join('images','Character', 'Right', 'Standing Right.png')),
    "right_1": pygame.image.load(path_join('images','Character', 'Right', 'Right Running 1.png')),
    "right_2": pygame.image.load(path_join('images','Character', 'Right', 'Right Running 2.png')),

    "left_standing": pygame.image.load(path_join('images','Character', 'Left', 'Standing Left.png')),
    "left_1": pygame.image.load(path_join('images','Character', 'Left', 'Left Running 1.png')),
    "left_2": pygame.image.load(path_join('images','Character', 'Left', 'Left Running 2.png')),

    "up_standing": pygame.image.load(path_join('images','Character', 'Backward', 'Standing Backward.png')),
    "up_1": pygame.image.load(path_join('images','Character', 'Backward', 'Backward Running 1.png')),
    "up_2": pygame.image.load(path_join('images','Character', 'Backward', 'Backward Running 2.png')),

    "down_standing": pygame.image.load(path_join('images','Character', 'Forward', 'Standing Forward.png')),
    "down_1": pygame.image.load(path_join('images','Character', 'Forward', 'Forward Running 1.png')),
    "down_2": pygame.image.load(path_join('images','Character', 'Forward', 'Forward Running 2.png')),
}

""" A List to set how many viruses their attributes """
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
    {
        "starting_x": 510,
        "starting_y": 360,
        "velocity": 10,
    },
]

""" Virus sprites for easy access to each sprite """
VIRUS_SPRITES = {
    "right": pygame.image.load(path_join('images','Virus.png')),
    "left": pygame.image.load(path_join('images','Virus.png')),
    "up": pygame.image.load(path_join('images','Virus.png')),
    "down": pygame.image.load(path_join('images','Virus.png')),
    "down_standing": pygame.image.load(path_join('images','Virus.png')),
}
# car sprite from https://www.pinterest.ca/pin/233624299398167646/

""" Sprites for easy access to each sprite.
    Includes Obstacles and Loot """
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
    "heart": pygame.image.load(path_join('images', 'heart sprite.png')),
}

""" Background sprite """
BACKGROUND = pygame.image.load(path_join('images','background.png'))

""" Icon sprite """
ICON = pygame.image.load(path_join('images','chase2.png'))

""" Layered Level map for the 1st Floor """
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

""" Layered Level map for the 2nd Floor """
WALL_LIST_2ND_FLOOR = {
    "loot":
    [
        "                                        ",
        "                                        ",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W==============S==========S====WWWWW===W",
        "W==WWWWWWW=====S=#S###S#==S============W",
        "W==WH==========S==S=H=S===S==S===S==S==W",
        "W==W=====WW====S==S===S===S==S===S==S==W",
        "W==WWWWW=W=====S==S=S=S===SS=====S==S==W",
        "W========W==========S=========#========W",
        "W===========S##====########==##=######=W",
        "W########===S=================#========W",
        "W===========#######===####=======#===#=W",
        "W=============S===========S==###=###=##W",
        "W==###====S###==########==S====#===#===W",
        "W========#S============================W",
        "W===========================###==#####=W",
        "W=######==####S==######===========#====W",
        "W=========#===S==#=====================W",
        "W=========##=====#===###===###########SW",
        "W#######==============================SW",
        "W============S==S==S==S==S============SW",
        "W==###===S===S==S==S==S==SS==S==S==S==SW",
        "W===H====S===S==S=====S==SS==S==S==S==SW",
        "W=#####==S===S==S=W==WS==SS==S==S==S==SW",
        "W=================W==WS==============HSW",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
    "virus":
    [
        "                                        ",
        "                                        ",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W+l=======l+ll+S+l=l+l==l+S====WWWWW+l+W",
        "Wl=WWWWWWW=l==lSl#S###S#=lS=+ll+ll+l==lW",
        "W==W+l=l+l===l+S+=S=H=S===S=lS=l=Sl=S==W",
        "W==W====lWW===lSl=S+l+S===S==S===S==S==W",
        "W==WWWWW=W====lSl=SlSlS==lSSl==l=Sl=S=lW",
        "Wl======lW=l==+l+ll+S+l=l+ll+=#+ll+l=l+W",
        "W+l====l+ll+S##=l==########=l##=######lW",
        "W########==lS+ll+l=l+l=====l+=#=+l=l+l+W",
        "W+l==l+l+ll+#######=l=####==l===l#==l#=W",
        "Wl====l=l=====S+l==l+l=l+=S+=###=###=##W",
        "W==###====S###=l########l=Sl===#l==#l==W",
        "Wl====l==#S+l==l=======l+l=l+l=l+l=l+l+W",
        "W+l==l+l+l====l+l=======l=l+###=l#####lW",
        "Wl######==####S==######=l==l====l=#====W",
        "Wl======l=#=+=S==#+l+l=l+ll+l==l+l===l+W",
        "W+l====l+=##l=+==#l=l###l==###########SW",
        "W#######l==+l=l=l+ll+l=l+ll+ll+ll+l=l+SW",
        "W+l====l+l=l+S==Sl=S==S=lS=l==l==l===lSW",
        "Wl=###==lS===S==S=lSl=S==SS==S==S==S==SW",
        "W+l=H==l+S===S==S=+l+=S==SS==S==S==S==SW",
        "Wl#####=lS=l=Sl=SlW==WS=lSSl=Sl=Sl=S=lSW",
        "W+l====l+ll+ll+ll+W==WS=+ll+ll+ll+l=l+SW",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
}

""" Layered Level map for the Parking Lot """
WALL_LIST_PARKING_LOT = {
    "loot":
        [
            "                                        ",
            "                                        ",
            "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
            "TC==========R==================HR======T",
            "T======C=====CC====C==========C=C======T",
            "T===RRRR=RR======RRR=RRRRRRRRRr====RRRRT",
            "T==C=====CC=CC=====C==========r========T",
            "T=========R==C=====C=========CrC=======T",
            "T====r=R=====R=R==CC====RRRR=====rRRRRRT",
            "T==r=r=Hr====C============CC==r==r=====T",
            "T==r==R=r=C======rC==RRRR=RR==r==r===C=T",
            "T==r====r=R=======RRRR=====C==r=====C==T",
            "T=====CC==RRR===========R==========R===T",
            "T===C========r=========RCR==Cr==r==RRRRT",
            "T==RR=RRRRRRRR===C===========r==r======T",
            "T=====r==========CC===C===C==r==r=rRRR=T",
            "T========C====C===C====RRRR==r====r====T",
            "T==rRRR=RR=CRR==C============rC===r=R==T",
            "T==r=Hr==C=CRR==C==RR==RR===RRR=====C==T",
            "T==r==r====C==C====R=============RR====T",
            "T==r===========================rRRRRrRRT",
            "T==rRRRRRC===RRr=======RRRRRR==r====r==T",
            "T==r==========Cr==r==rr========r=C=Hr==T",
            "T=====RRR===C==r==r==rr=C==R===rR==CrC=T",
            "T====C======C=====r==r==C==============T",
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
            "TC+l===l+ll+R+ll+l=l+l==l+l==l+HR=+l=l+T",
            "T+l==l+Cl==l=CC=l==Cl=========C=C=l====T",
            "Tl==RRRR=RR+ll+l+RRRlRRRRRRRRRr=+l+RRRRT",
            "Tl=C=====CC=CCl=l==C+l=====l+=r=l=l====T",
            "T+ll+l+ll+R==C+l+l+Cl=======lCrCl=+l=l+T",
            "Tl==lrlR+l=l+RlRl=CCl===RRRR+l=l+rRRRRRT",
            "T==r+r+Hr===lCl=+l=l+l==l+CCl=r=lr+l=l+T",
            "T==r=+R=r=C=+l+l+rC==RRRRlRR==r==rl==ClT",
            "Tl=r=l==r=R===l=l=RRRR===l=Cl=r=l=l=C=lT",
            "T+l=l+CC=lRRR=+l=l+ll+l+R+ll+l+l+l+R+l+T",
            "Tl==Cl=+l+ll+rl===l==l=RCR==Crl=r=lRRRRT",
            "T==RR=RRRRRRRRl=lC+ll+l====l+r==r=+l=l+T",
            "T=l==lr+ll+l=l+l+CC==lC===C=lrl=r=rRRRlT",
            "T=+ll+=l=Cl===C===C==l=RRRR=lr+ll+r+ll+T",
            "T==rRRR=RR=CRR=+C+l=l+l==l+l+rC==lrlR=lT",
            "T==r+=r==C=CRR=lCl=RRl=RR=l=RRR+l+l+C=lT",
            "T==rl=rl==lC==Cl=l=R=l====l======RR=+l+T",
            "T==r+ll+ll+l+ll+l+l=l+===l+l=l+rRRRRrRRT",
            "T==rRRRRRCl=lRRr=l=====RRRRRR=lr+l+=r=+T",
            "T==r+l===l+l++Cr==r==rr+ll+l=l+r=ClHr=lT",
            "Tl==l=RRR=l=Cl=r=lr==rrlC=lR==lrR=lCrClT",
            "T+ll+C+l=l+=C+l=l+r==r=+C=+l=l+l=l+l=l+T",
            "TTTTTTTTTTTTTTTTTTT==TTTTTTTTTTTTTTTTTTT",
        ],
}

""" A list containing all the levels maps """
LEVEL_LIST = [WALL_LIST_PARKING_LOT, WALL_LIST_1ST_FLOOR, WALL_LIST_2ND_FLOOR]
