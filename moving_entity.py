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
    """ Moving Entity Class """
    def __init__(self, game_ref, sprite_setting, entity_settings, default_sprite: str = None):
        """ Moving Entity Constructor """
        if type(game_ref) is not game.Game:
            raise TypeError("invalid reference")

        super().__init__()

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

        if default_sprite == None:
            self.image = self.sprite_setting['down'].convert_alpha()
        elif default_sprite not in sprite_setting:
            raise ValueError(f"Invalid default sprite: {default_sprite}")
        else:
            self.image = self.sprite_setting[default_sprite].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.entity_settings["starting_x"]
        self.rect.y = self.entity_settings["starting_y"]

    def redraw(self):
        """ Displays itself on the window """
        for direction in self.directions:
            if self.directions[direction]:
                self.image = self.sprite_setting[direction].convert_alpha()
        self.game_ref.window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        """ Abstract Method """
        pass

    def is_in_bounds(self, side: str):
        """ Checks if the Entities next move towards a side will take it out of the window """
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
        """ Checks if the Entities next move towards a side will make it collide with an obstacle """
        if side in ["left", "up"]:
            velocity = -self.velocity
        else:
            velocity = self.velocity
        
        temp_sprite = pygame.sprite.Sprite()
        temp_sprite.image = self.sprite_setting['down_standing'].convert_alpha()
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
        """ Checks if the Entity can move in a certain direction """
        return self.directions[move_direction] and self.is_in_bounds(move_direction) and not self.will_hit_wall(move_direction)

    def align_with_wall(self, side, wall):
        """ Aligns one edge of the Entity with an edge of the Wall """
        if side == "left":
            self.rect.left = wall.rect.right
        elif side == "right":
            self.rect.right = wall.rect.left
        elif side == "up":
            self.rect.top = wall.rect.bottom
        elif side == "down":
            self.rect.bottom = wall.rect.top

    def move(self):
        """ Abstract Method """
        pass
    
    def switch_directions(self, key):
        """ Abstract Method """
        pass
