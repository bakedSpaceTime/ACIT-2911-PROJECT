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
from settings import GAME_SETTINGS, BACKGROUND, WALL_LIST_1ST_FLOOR, VIRUS_SETTINS
from player import Player
from virus import Virus
from wall import Wall, Shelf
from loot import ToiletPaper, HandSanitizer


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
        self.sanitizer_list = pygame.sprite.Group()

        self.create_walls()
        self.create_loots()
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

    def create_loots(self):
        for y, line in enumerate(WALL_LIST_1ST_FLOOR):
            for x, char in enumerate(line):
                if char == '=':
                    paper = ToiletPaper(x * 30, y * 30)
                    self.toilet_list.add(paper)
                    self.all_sprite_list.add(paper)
                if char == 'H':
                    sanitizer = HandSanitizer(x * 30, y * 30)
                    self.sanitizer_list.add(sanitizer)
                    self.all_sprite_list.add(sanitizer)

    def create_walls(self):
        for y, line in enumerate(WALL_LIST_1ST_FLOOR):
            for x, char in enumerate(line):
                if char == '#':
                    shelf = Shelf(x * 30, y * 30)
                    self.wall_list.add(shelf)
                    self.all_sprite_list.add(shelf)
                if char == 'S':
                    shelf = Shelf(x * 30, y * 30, 'side')
                    self.wall_list.add(shelf)
                    self.all_sprite_list.add(shelf)
                if char == 'W':
                    wall = Wall(x * 30, y * 30)
                    self.wall_list.add(wall)
                    self.all_sprite_list.add(wall)

    def create_virus(self):
        for i in range(len(VIRUS_SETTINS)):
            virus = Virus(self, i)
            self.virus_list.add(virus)
            self.all_sprite_list.add(virus)
