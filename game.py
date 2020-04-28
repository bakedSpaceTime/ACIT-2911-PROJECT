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
from settings import GAME_SETTINGS
from player import Player
from wall import Wall

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

        self.create_walls()
  
    def main_game(self):
        while True:
            self.window.fill((0, 0, 0))

            self.clock.tick(30)
            self.player.update()
            self.all_sprite_list.update()
            self.all_sprite_list.draw(self.window)
            pygame.display.update()
            

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

        wall = Wall(450, 450, 400, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(50, 100, 400, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(50, 100, 10, 400)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)
