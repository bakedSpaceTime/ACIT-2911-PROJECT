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
from settings import GAME_SETTINGS, PLAYER_SETTINS

class Player():
    def __init__(self, game_ref):

        self.game_ref = game_ref
        
        self.x_pos = PLAYER_SETTINS["starting_x"]
        self.y_pos = PLAYER_SETTINS["starting_y"]
        self.velocity = PLAYER_SETTINS["velocity"]
        self.directions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

        self.width = PLAYER_SETTINS["sprite_width"]
        self.height = PLAYER_SETTINS["sprite_height"]

        self.char = pygame.image.load('images/pac-right.bmp')
        self.charRight = pygame.image.load('images/pac-right.bmp')
        self.charLeft = pygame.image.load('images/pac-left.bmp')
        self.charUp = pygame.image.load('images/pac-up.bmp')
        self.charDown = pygame.image.load('images/pac-down.bmp')

    def redraw(self):
        self.game_ref.window.fill((0, 0, 0))

        if self.directions["left"]:
            self.game_ref.window.blit(self.charLeft, (self.x_pos,self.y_pos))
        elif self.directions["right"]:
            self.game_ref.window.blit(self.charRight, (self.x_pos,self.y_pos))
        elif self.directions["up"]:
            self.game_ref.window.blit(self.charUp, (self.x_pos,self.y_pos))
        elif self.directions["down"]:
            self.game_ref.window.blit(self.charDown, (self.x_pos, self.y_pos))
        else:
            self.game_ref.window.blit(self.char, (self.x_pos, self.y_pos))

        pygame.display.update()

    def update(self):

        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                if e.type == pygame.KEYDOWN:
                    self.switch_directions(e.key)

        self.move_player()
        self.redraw()

    def is_in_bounds(self, side: str):
        boundries = {
            "left": self.x_pos > 0 + self.velocity,
            "right": self.x_pos < GAME_SETTINGS['width'] - self.width - self.velocity,
            "up": self.y_pos > 0 + self.velocity,
            "down": self.y_pos < GAME_SETTINGS['height'] - self.height - self.velocity,
        }

        if side not in boundries.keys():
            raise ValueError("Valid bountries are 'left', 'right', 'up', 'down'.")

        return boundries[side]

    def switch_directions(self, key):
        key_str = self.key_to_direction_str(key)
        if key_str in self.directions.keys():
            for direction in self.directions:
                if direction == key_str:
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False

    def move_player(self):

        if self.directions["left"] and self.is_in_bounds("left"):
            self.x_pos -= self.velocity
        elif self.directions["right"] and self.is_in_bounds("right"):
            self.x_pos += self.velocity
        elif self.directions["up"] and self.is_in_bounds("up"):
            self.y_pos -= self.velocity
        elif self.directions["down"] and self.is_in_bounds("down"):
            self.y_pos += self.velocity
    
    @staticmethod
    def key_to_direction_str(key):
        out_str = ""
        if key == pygame.K_LEFT:
            out_str = "left"
        elif key == pygame.K_RIGHT:
            out_str = "right"
        elif key == pygame.K_UP:
            out_str = "up"
        elif key == pygame.K_DOWN:
            out_str = "down"
        return out_str