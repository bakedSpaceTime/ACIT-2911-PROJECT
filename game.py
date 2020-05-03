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
from settings import GAME_SETTINGS, BACKGROUND
from player import Player
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

        self.create_walls()
        self.create_toilets()

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
        i = 20

        while i < 450:
            j = 20
            while j < 450:
                paper = ToiletPaper(i, j)
                self.toilet_list.add(paper)
                self.all_sprite_list.add(paper)
                j += 60
            i += 60

    def create_walls(self):
        wall = Wall(0, 0, 10, 500)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(0, 490, 500, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(490, 0, 10, 500)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(0, 0, 500, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(0, 50, 450, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(0, 100, 450, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(50, 150, 10, 450)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(110, 150, 10, 450)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(170, 150, 10, 450)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(230, 150, 10, 450)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(290, 150, 10, 450)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(350, 150, 10, 450)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(410, 150, 10, 450)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)
