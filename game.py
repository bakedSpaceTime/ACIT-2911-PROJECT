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

        wall = Wall(0, 0, 30, 500)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(0, 480, 500, 30)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(480, 0, 30, 500)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(0, 0, 500, 30)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(0, 60, 450, 30)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(0, 120, 450, 10)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(60, 180, 30, 300)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(120, 180, 10, 450)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(180, 180, 10, 450)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(240, 180, 10, 450)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(300, 180, 10, 450)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(360, 180, 10, 450)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)

        wall = Wall(420, 180, 10, 450)
        self.wall_list.add(wall.shelf_list)
        self.all_sprite_list.add(wall.shelf_list)
