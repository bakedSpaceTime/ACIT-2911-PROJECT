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
from settings import GAME_SETTINGS, PLAYER_SETTINS, PLAYER_SPRITES
from moving_entity import MovingEntity


class Player(MovingEntity):
    def __init__(self, game_ref):

        if type(game_ref) is not game.Game:
            raise TypeError("invalid reference")

        super().__init__(game_ref, PLAYER_SPRITES, PLAYER_SETTINS)

    def move(self):
        item_hit_list = pygame.sprite.spritecollide(self, self.game_ref.toilet_list, False)
        for toilet_paper in item_hit_list:
            self.game_ref.toilet_list.remove(toilet_paper)
            self.game_ref.all_sprite_list.remove(toilet_paper)
            self.score += 1
            print("item", toilet_paper)
            print("item_hit_list", len(self.game_ref.toilet_list))
            print("score: ", self.score)

        if self.directions["left"] and self.is_in_bounds("left") and not self.will_hit_wall("left"):
            self.rect.x -= self.velocity
        elif self.directions["right"] and self.is_in_bounds("right") and not self.will_hit_wall("right"):
            self.rect.x += self.velocity
        elif self.directions["up"] and self.is_in_bounds("up") and not self.will_hit_wall("up"):
            self.rect.y -= self.velocity
        elif self.directions["down"] and self.is_in_bounds("down") and not self.will_hit_wall("down"):
            self.rect.y += self.velocity
