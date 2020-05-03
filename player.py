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

        super().__init__(game_ref, PLAYER_SPRITES, PLAYER_SETTINS, "standing_down")
        
        self.lives = PLAYER_SETTINS["lives"]
        self.score = 0

        # If hand sanitizer is picked up
        self.boosted = False

    def update(self):

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                self.switch_directions(e.key)

        self.move()
        self.redraw()

    def move(self):
        self.collision_handler()

        if self.is_valid_direction("left"):
            self.rect.x -= self.velocity
        elif self.is_valid_direction("right"):
            self.rect.x += self.velocity
        elif self.is_valid_direction("up"):
            self.rect.y -= self.velocity
        elif self.is_valid_direction("down"):
            self.rect.y += self.velocity
    
    def switch_directions(self, key):
        key_str = self.key_to_direction_str(key)
        if key_str in self.directions.keys():
            for direction in self.directions:
                if direction == key_str:
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False

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

    def collision_handler(self):
        self.collect_toilet_paper()
        self.check_virus()

    def collect_toilet_paper(self):
        item_hit_list = pygame.sprite.spritecollide(self, self.game_ref.toilet_list, False)
        for toilet_paper in item_hit_list:
            self.game_ref.toilet_list.remove(toilet_paper)
            self.game_ref.all_sprite_list.remove(toilet_paper)
            self.score += 1

    def check_virus(self):
        item_hit_list = pygame.sprite.spritecollide(self, self.game_ref.virus_list, False)
        if not self.boosted and len(item_hit_list) != 0:
            self.loose_life()

    def loose_life(self):
        self.lives -= 1
        # print(f"Lives: {self.lives}")
