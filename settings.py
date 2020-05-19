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
        "W=================W==WS==============HSW",
        "WWWWWWWWWWWWWWWWWWW==WWWWWWWWWWWWWWWWWWW",
    ],
    "virus":
    [
        "                                        ",
        "                                        ",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "Waq=======qaqqaSaq=qaq==qaS====WWWWWaqaW",
        "Wq=WWWWWWW=q==qSq#S###S#=qS=aqqaqqaq==qW",
        "W==Waq=qaq===qaSa=S=H=S===S=qS=q=Sq=S==W",
        "W==W====qWW===qSq=SaqaS===S==S===S==S==W",
        "W==WWWWW=W====qSq=SqSqS==qSSq==q=Sq=S=qW",
        "Wq======qW=q==aqaqqaSaq=qaqqa=#aqqaq=qaW",
        "Waq====qaqqaS##=q==########=q##=######qW",
        "W########==qSaqqaq=qaq=====qa=#=aq=qaqaW",
        "Waq==qaqaqqa#######=q=####==q===q#==q#=W",
        "Wq====q=q=====Saq==qaq=qa=Sa=###=###=##W",
        "W==###====S###=q########q=Sq===#q==#q==W",
        "Wq====q==#Saq==q=======qaq=qaq=qaq=qaqaW",
        "Waq==qaqaq====qaq=======q=qa###=q#####qW",
        "Wq######==####S==######=q==q====q=#====W",
        "Wq======q=#=a=S==#aqaq=qaqqaq==qaq===qaW",
        "Waq====qa=##q=a==#q=q###q==###########SW",
        "W#######q==aq=q=qaqqaq=qaqqaqqaqqaq=qaSW",
        "Waq====qaq=qaS==Sq=S==S=qS=q==q==q===qSW",
        "Wq=###==qS===S==S=qSq=S==SS==S==S==S==SW",
        "Waq=H==qaS===S==S=aqa=S==SS==S==S==S==SW",
        "Wq#####=qS=q=Sq=SqW==WS=qSSq=Sq=Sq=S=qSW",
        "Waq====qaqqaqqaqqaW==WS=aqqaqqaqqaq=qaSW",
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
        ],
    "virus":
        [
            "                                        ",
            "                                        ",
            "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
            "TCaq===qaqqaRaqqaq=qaq==qaq==qaHR=aq=qaT",
            "Taq==qaCq==q=CC=q==Cq=========C=C=q====T",
            "Tq==RRRR=RRaqqaqaRRRqRRRRRRRRRr=aqaRRRRT",
            "Tq=C=====CC=CCq=q==Caq=====qa=r=q=q====T",
            "TaqqaqaqqaR==CaqaqaCq=======qCrCq=aq=qaT",
            "Tq==qrqRaq=qaRqRq=CCq===RRRRaq=qarRRRRRT",
            "T==raraHr===qCq=aq=qaq==qaCCq=r=qraq=qaT",
            "T==r=aR=r=C=aqaqarC==RRRRqRR==r==rq==CqT",
            "Tq=r=q==r=R===q=q=RRRR===q=Cq=r=q=q=C=qT",
            "Taq=qaCC=qRRR=aq=qaqqaqaRaqqaqaqaqaRaqaT",
            "Tq==Cq=aqaqqarq===q==q=RCR==Crq=r=qRRRRT",
            "T==RR=RRRRRRRRq=qCaqqaq====qar==r=aq=qaT",
            "T=q==qraqqaq=qaqaCC==qC===C=qrq=r=rRRRqT",
            "T=aqqa=q=Cq===C===C==q=RRRR=qraqqaraqqaT",
            "T==rRRR=RR=CRR=aCaq=qaq==qaqarC==qrqR=qT",
            "T==ra=r==C=CRR=qCq=RRq=RR=q=RRRaqaqaC=qT",
            "T==rq=rq==qC==Cq=q=R=q====q======RR=aqaT",
            "T==raqqaqqaqaqqaqaq=qa===qaq=qarRRRRrRRT",
            "T==rRRRRRCq=qRRr=q=====RRRRRR=qraqa=r=aT",
            "T==raq===qaqaaCr==r==rraqqaq=qar=CqHr=qT",
            "Tq==q=RRR=q=Cq=r=qr==rrqC=qR==qrR=qCrCqT",
            "TaqqaCaq=qa=Caq=qar==r=aC=aq=qaq=qaq=qaT",
            "TTTTTTTTTTTTTTTTTTT==TTTTTTTTTTTTTTTTTTT",
        ],
}
