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
    "velocity": 8,
    "lives": 10,
    "boosted_duration": 5,
    "invincible_duration": 2,
}

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

VIRUS_SPRITES = {
    "right": pygame.image.load(path_join('images','Virus.png')),
    "left": pygame.image.load(path_join('images','Virus.png')),
    "up": pygame.image.load(path_join('images','Virus.png')),
    "down": pygame.image.load(path_join('images','Virus.png')),
    "down_standing": pygame.image.load(path_join('images','Virus.png')),
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
    "heart": pygame.image.load(path_join('images', 'heart sprite.png')),
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
        "W=================W==W===S===========HSW",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
    "virus":
    [
        "                                        ",
        "                                        ",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W++l=====l+++++S+l=====l++S++l+WWWWW+++W",
        "WllWWWWWWW+++++Sl#S###S#llS++l+++l+++++W",
        "W==W+l=l+l+++++S=+S+l+S+++SllSlllSllSllW",
        "W==W+l=l+WWllllS=lS+l+SlllS++SlllS==S==W",
        "WllWWWWW+W+++++SllSlSlSlllSS+++++SllSllW",
        "W++l===l+W++++++++++S+l+++l+++#++l+++++W",
        "W++l===l++++S##llll########ll##l######lW",
        "W########lllS+l+++++++l==l++++#++l+l+l+W",
        "W++l=l+l+ll+#######lll####++++l++#+l+#+W",
        "W++l==ll+l++l+S+l==+++=l++Sll###l###l##W",
        "Wll###l=l+S###++########llS++++#+l+#+l+W",
        "W+l=l++l+#S+l+ll+=====l+l=+++++++l+l+l+W",
        "W+++l++l++l+l++++l====l+l=l+###ll#####lW",
        "Wl######ll####S==######++l++++++++#++++W",
        "W+l=l+l=l+#+++Sll#+++ll+++++++++++l++++W",
        "W+l=l+l=l+##+++++#lll###lll###########SW",
        "W#######++++++++++++++l++++++l++l++l++SW",
        "W++l====l+ll+SllSllSllSllS+ll=ll=ll=l+SW",
        "Wll###===S==lS==S=lSllS==SS++S++S++S+lSW",
        "W++l===++S===S==S++l++S==SS++S++S++S++SW",
        "Wl#####llSlllSllSlW==WSllSSllSllSllSllSW",
        "W+l===l++l+++l++l+W==W+++S+++l++l++l++SW",
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
            "T======C=====CC====C==========C=C======T",
            "T===RRRR=RR======RRR=RRRRRRRRRr====RRRRT",
            "T==C=====CC=CC=====C==========r========T",
            "T====r====R==C=====C=========CrC=======T",
            "T====r=R=====R=R==CC====RRRR=====rRRRRRT",
            "T==r=r=Hr====C============C===r==r=====T",
            "T==r==R=r=C======rC==RRRR=RR==r==r===C=T",
            "T==r====r=R=======RRRR=====C==r=====C==T",
            "T=====CC==RRR===========R==========R===T",
            "T===C========r=========RCR==Cr==r==RRRRT",
            "T==RR=RRRRRRRR===C===========r==r======T",
            "T=====r==========CC===C===C==r==r=rRRR=T",
            "T========C====C===C====RRRR==r====r====T",
            "T==rRRRRRR=CRR==C============rC===r=R==T",
            "T==rH=r==C=CRR==C==RR==RR===RRRR====C==T",
            "T==r==r====C==C====R=============RR====T",
            "T==r=======================C===rRRRRrRRT",
            "T==rRRRRRC===RRr=======RRRRRR==r====r==T",
            "T==r==========Cr==r==rr========r=C=Hr==T",
            "T=====RRR===C==r==r==rr=C==R===rR==CrC=T",
            "T====C======C=====r==r==C==============T",
            "TTTTTTTTTTTTTTTTTTT==TTTTTTTTTTTTTTTTTTT",
        ],
    "virus":
        [
            "                                        ",
            "                                        ",
            "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
            "TC+l=l+l+ll+R+l++l+l+l=l+l==l++HR++l=l+T",
            "T++l=l+C+ll++CC++l+C+l=l+l==l+C+C++l=l+T",
            "Tll=RRRRlRR++l+++RRRlRRRRRRRRRr++++RRRRT",
            "TllC+l+l+CClCC+++++C++++l==l++r++++l=l+T",
            "T++++r+l++R++C+++++C++++l==l+CrC+++l=l+T",
            "T++++rlR++l++R+RllCCllllRRRR++l++rRRRRRT",
            "Tllrlr+Hr+l++C++++++++++++C+++rllr+++l+T",
            "T++r++R+rlC++++++rC++RRRRlRRllrllr+++ClT",
            "Tllr++l+rlR+++++++RRRR++l++Cllr+++++C++T",
            "T+++++CC++RRR+++++++++++R++++++++++R+++T",
            "T+++C+ll++ll+r+++++++++RCRllCrllrllRRRRT",
            "TllRRlRRRRRRRRlllC++++++l++++r++r++l=l+T",
            "T+++++r++l+ll++++CClllC+l+CllrllrlrRRRlT",
            "T+++++l++C+ll+C+++C++++RRRRllr++++r+l++T",
            "TllrRRRRRRlCRR++C++++++ll++++rC+++rlRllT",
            "T==rH=r++C+CRR++CllRRllRRlllRRRR++l+CllT",
            "Tllr+=rll=lC++C++++R+++ll++++++l+RR+l++T",
            "T++r++l++++l++l+l++++++ll++C+++rRRRRrRRT",
            "TllrRRRRRC+l+RRr+++++++RRRRRR++r+l++r++T",
            "Tllr++l=l+++++Crllrqqrr+l++l+l+r+ClHr++T",
            "T+++++RRRlllC++r++r++rrlC++R+l+rR++CrClT",
            "T++++C+ll+++C++l++r==r++C++l+++ll++==l+T",
            "TTTTTTTTTTTTTTTTTTT==TTTTTTTTTTTTTTTTTTT",
        ],
}
