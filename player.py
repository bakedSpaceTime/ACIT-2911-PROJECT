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
import sys
import pygame
import game
import threading
import time
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
        self.vulnerable = True

    def update(self):

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
        self.collect_hand_sanitizer()
        self.check_virus()

    def collect_toilet_paper(self):
        item_hit_list = pygame.sprite.spritecollide(self, self.game_ref.toilet_list, False)
        for toilet_paper in item_hit_list:
            self.game_ref.toilet_list.remove(toilet_paper)
            self.game_ref.all_sprite_list.remove(toilet_paper)
            self.score += 1

    def collect_hand_sanitizer(self):
        item_hit_list = pygame.sprite.spritecollide(self, self.game_ref.sanitizer_list, False)
        for sanitizer in item_hit_list:
            self.boosted = True
            self.game_ref.sanitizer_list.remove(sanitizer)
            self.game_ref.all_sprite_list.remove(sanitizer)
            t = threading.Timer(PLAYER_SETTINS["boosted_duration"], self.back_to_normal)
            t.start()

    def check_virus(self):
        item_hit_list = pygame.sprite.spritecollide(self, self.game_ref.virus_list, False)
        if not self.boosted and len(item_hit_list) != 0 and self.vulnerable:
            self.vulnerable = False
            self.loose_life()
            t = threading.Timer(PLAYER_SETTINS["invincible_duration"], self.back_to_vulnerable)
            t.start()
        if self.boosted:
            for virus in item_hit_list:
                self.game_ref.virus_list.remove(virus)
                self.game_ref.all_sprite_list.remove(virus)

    def loose_life(self):
        if self.lives == 1:
            print("You ran out of lives!")
            time.sleep(5)
        self.lives -= 1
        print(f"Lives: {self.lives}")

    def back_to_vulnerable(self):
        self.vulnerable = True

    def back_to_normal(self):
        self.boosted = False
