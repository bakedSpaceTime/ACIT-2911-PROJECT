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
import game
from settings import GAME_SETTINGS


class MovingEntity(pygame.sprite.Sprite):
    def __init__(self, game_ref, sprite_setting, entity_settings):

        if type(game_ref) is not game.Game:
            raise TypeError("invalid reference")


        self.game_ref = game_ref
        self.sprite_setting = sprite_setting
        self.entity_settings = entity_settings

        self.velocity = entity_settings["velocity"]
        self.directions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

        self.image = self.sprite_setting['standing_down']
        self.rect = self.image.get_rect()
        self.rect.x = self.entity_settings["starting_x"]
        self.rect.y = self.entity_settings["starting_y"]
        self.score = 0

    def redraw(self):
        for direction in self.directions:
            if self.directions[direction]:
                self.image = self.sprite_setting[direction]
        self.game_ref.window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        pass
        # for e in pygame.event.get():
        #     if e.type == pygame.QUIT:
        #         pygame.quit()
        #     if e.type == pygame.KEYDOWN:
        #         self.switch_directions(e.key)

        # self.move()
        # self.redraw()

    def is_in_bounds(self, side: str):
        boundries = {
            "left": self.rect.x > 0 + self.velocity,
            "right": self.rect.x < GAME_SETTINGS['width'] - self.rect.width - self.velocity,
            "up": self.rect.y > 0 + self.velocity,
            "down": self.rect.y < GAME_SETTINGS['height'] - self.rect.height - self.velocity,
        }

        if side not in boundries.keys():
            raise ValueError("Valid bountries are 'left', 'right', 'up', 'down'.")

        return boundries[side]

    def will_hit_wall(self, side: str):
        if side in ["left", "up"]:
            velocity = -self.velocity
        else:
            velocity = self.velocity
        
        temp_sprite = pygame.sprite.Sprite()
        temp_sprite.image = self.sprite_setting['down']
        temp_sprite.rect = temp_sprite.image.get_rect()

        temp_sprite.rect = self.rect.copy()
        if side in ["left", "right"]:
        
            temp_sprite.rect.x += velocity

            block_hit_list = pygame.sprite.spritecollide(temp_sprite, self.game_ref.wall_list, False)
            if len(block_hit_list) > 0:
                self.align_with_wall(side, block_hit_list[0])
                return True

        temp_sprite.rect = self.rect.copy()
        if side in ["up", "down"]:
            temp_sprite.rect.y += velocity

            block_hit_list = pygame.sprite.spritecollide(temp_sprite, self.game_ref.wall_list, False)
            if len(block_hit_list) > 0:
                self.align_with_wall(side, block_hit_list[0])
                return True

    def is_valid_direction(self, move_direction):
        return self.directions[move_direction] and self.is_in_bounds(move_direction) and not self.will_hit_wall(move_direction)

    def align_with_wall(self, side, wall):
        if side == "left":
            self.rect.left = wall.rect.right
        elif side == "right":
            self.rect.right = wall.rect.left
        elif side == "up":
            self.rect.top = wall.rect.bottom
        elif side == "down":
            self.rect.bottom = wall.rect.top

    def switch_directions(self, key):
        key_str = self.key_to_direction_str(key)
        if key_str in self.directions.keys():
            for direction in self.directions:
                if direction == key_str:
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False

    def move(self):
        pass

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
