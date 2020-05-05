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
from settings import GAME_SETTINGS, BACKGROUND, WALL_LIST, VIRUS_SETTINS
from player import Player
from virus import Virus
from wall import Wall
from loot import ToiletPaper

class Game():
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode((GAME_SETTINGS['width'], GAME_SETTINGS['height']))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pandemic Run")

        self.player = Player(self)

        self.run = True

        self.all_sprite_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.toilet_list = pygame.sprite.Group()
        self.virus_list = pygame.sprite.Group()

        self.create_walls()
        self.create_toilets()
        self.create_virus()

        pygame.mixer.music.load('audio/bg.mp3')
        pygame.mixer.music.play(-1)
  
    def main_game(self):
        while True:
            self.window.fill((0, 0, 0))
            self.window.blit(BACKGROUND, (0,0))

            self.clock.tick(30)
            self.player.update()
            self.all_sprite_list.update()
            self.all_sprite_list.draw(self.window)
            pygame.display.update()

    def create_toilets(self):
        i = 30

        while i < 480:
            j = 30
            while j < 480:
                paper = ToiletPaper(i, j)
                self.toilet_list.add(paper)
                self.all_sprite_list.add(paper)
                j += 60
            i += 60

    def create_walls(self):

        for wall_rect in WALL_LIST:
            wall = Wall(wall_rect[0], wall_rect[1], wall_rect[2], wall_rect[3], )
            self.wall_list.add(wall.shelf_list)
            self.all_sprite_list.add(wall.shelf_list)

    def create_virus(self):
        for i in range(len(VIRUS_SETTINS)):
            virus = Virus(self, i)
            self.virus_list.add(virus)
            self.all_sprite_list.add(virus)
