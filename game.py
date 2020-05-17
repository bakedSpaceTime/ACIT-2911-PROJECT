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
import random
from settings import GAME_SETTINGS, BACKGROUND, VIRUS_SETTINS, PLAYER_SPRITES, OTHER_SPRITES, LEVEL_LIST
from player import Player
from virus import Virus
from wall import Obstacle
from loot import ToiletPaper, HandSanitizer
from text_box import TextBox
from button import Button
from send_score import send_score
from tkinter import messagebox, Tk
import webbrowser
from start_menu import StartMenu
from pause_menu import PauseMenu
from end_menu import EndMenu
from timer import Timer
from statistics import mean



class Game:

    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode((GAME_SETTINGS['width'], GAME_SETTINGS['height']))
        BACKGROUND.convert_alpha()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pandemic Run")
        #self.level = WALL_LIST_1ST_FLOOR
        #self.level = WALL_LIST_PARKING_LOT
        # self.level = WALL_LIST_2ND_FLOOR
        self.start_menu = StartMenu(self)
        self.pause_menu = PauseMenu(self)
        self.game_over = EndMenu(self)
        self.state = None
        self.player = None
        self.heart_list = None
        self.level = None
        self.run = False
        self.time = None
        # self.new_game()

        self.run = False
        self.frame_count = 1
        self._initialize_music()
        self.state = "start"

        self.all_sprite_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.toilet_list = pygame.sprite.Group()
        self.virus_list = pygame.sprite.Group()
        self.sanitizer_list = pygame.sprite.Group()

        self.stats = []

    def begin_new_game(self):
        self.player = Player(self)
        self.heart_list = []
        self.level_index = 0
        self.initialize_map(level=LEVEL_LIST[self.level_index])
        self.fade_in_screen(GAME_SETTINGS["width"], GAME_SETTINGS["height"])

        self.time = Timer()
        self.time.start()
        self.state = "game"

    def initialize_map(self, level=LEVEL_LIST[0]):
        self.level = level
        self.run = True
        # self.all_sprite_list = pygame.sprite.Group()
        # self.wall_list = pygame.sprite.Group()
        # self.toilet_list = pygame.sprite.Group()
        # self.virus_list = pygame.sprite.Group()
        # self.sanitizer_list = pygame.sprite.Group()
        self.sanitizer_icon = Icon((GAME_SETTINGS["width"] / 36), 0, "sanitizer_icon")

        self.create_walls()
        self.create_loots()
        self.create_virus()
        self.create_status_icons()

    def main_game(self):
        while True:
            self.window.fill((0, 0, 0))
            self.clock.tick(30)

            if self.state == "start":
                self.start_menu.update()
            if self.state == "game":
               self.game_controller()
            elif self.state == "pause":
                self.pause_menu.update()
            elif self.state == "game_over":
                self.game_over.update()
            elif self.state == "restart":
                self.begin_new_game()

            pygame.display.update()

            # print(self.clock.get_fps())

            self.frame_count += 1
            if self.frame_count > 30:
                self.frame_count = 1

    def redraw_screen(self):
        # self.window.blit(BACKGROUND.convert_alpha(), (0, 0))
        # self.player.update()
        self.window.blit(BACKGROUND, (0, 0))
        self.all_sprite_list.draw(self.window)

    def game_controller(self):
        self.redraw_screen()
        self.player.update()
        self.virus_list.update()

        if len(self.toilet_list) == 0:
            self.increment_level()

    def increment_level(self):
        self.fade_out_screen(GAME_SETTINGS["width"], GAME_SETTINGS["height"])
        pygame.time.delay(250)
        self.all_sprite_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.toilet_list = pygame.sprite.Group()
        self.virus_list = pygame.sprite.Group()
        self.sanitizer_list = pygame.sprite.Group()
        self.player.restart_position()
        self.level_index += 1
        if self.level_index >= len(LEVEL_LIST): 
            self.state = "game_over"
        else:
            self.initialize_map(LEVEL_LIST[self.level_index])
        self.fade_in_screen(GAME_SETTINGS["width"], GAME_SETTINGS["height"])

    def kill_viruses(self):
        for virus in self.virus_list:
            self.all_sprite_list.remove(virus)
            self.virus_list.remove(virus)

    def fade_out_screen(self, width, height):
        fade = pygame.Surface((width, height))
        fade.fill((0, 0, 0))
        for a in range(0, 255, 5):
            fade.set_alpha(a)
            self.redraw_screen()
            self.window.blit(fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5)

    def fade_in_screen(self, width, height):
        fade = pygame.Surface((width, height))
        fade.fill((0, 0, 0))
        for a in range(255, 0, -5):
            fade.set_alpha(a)
            self.window.blit(BACKGROUND.convert_alpha(), (0, 0))

            self.redraw_screen()
            self.window.blit(fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5)


    def _initialize_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load('audio/bg.mp3')
        pygame.mixer.music.play(-1)

    def create_loots(self):
        for y, line in enumerate(self.level["loot"]):
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
        for y, line in enumerate(self.level["loot"]):
            if y <= 1:
                continue
            for x, char in enumerate(line):
                if char == '#':
                    obstacle = Obstacle(x * 30, y * 30, "shelf_front")
                if char == 'S':
                    obstacle = Obstacle(x * 30, y * 30, "shelf_side")
                if char == 'W':
                    obstacle = Obstacle(x * 30, y * 30)
                if char == 'R':
                    obstacle = Obstacle(x * 30, y * 30, "railing_front")
                if char == 'r':
                    obstacle = Obstacle(x * 30, y * 30, "railing_side")
                if char == 'T':
                    obstacle = Obstacle(x * 30, y * 30, "tree")
                if char == 'C':
                    obstacle = Obstacle(x * 30, y * 30, f"car{random.randint(1, 3)}")
                self.wall_list.add(obstacle)
                self.all_sprite_list.add(obstacle)

    def create_virus(self):
        for i in range(len(VIRUS_SETTINS)):
            virus = Virus(self, i, self.level["virus"])
            self.virus_list.add(virus)
            # self.all_sprite_list.add(virus)

    def create_sanitizer_icon(self):
        self.all_sprite_list.add(self.sanitizer_icon)

    def create_status_icons(self):
        paper = Icon((GAME_SETTINGS["width"] / 9), 5, "paper_icon")
        self.all_sprite_list.add(paper)

        for i in range(self.player.lives):
            if i % 2 == 1:
                heart = Heart((GAME_SETTINGS["width"] / 8) * 7 + ((i-1) * 15), 0 + 30)
            else:
                heart = Heart((GAME_SETTINGS["width"] / 8) * 7 + (i * 15), 0)
            self.heart_list.append(heart)
            self.all_sprite_list.add(heart)

class Icon(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = OTHER_SPRITES[type]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = OTHER_SPRITES["heart"]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
