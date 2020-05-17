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
import threading
import time
from settings import GAME_SETTINGS, PLAYER_SETTINS, PLAYER_SPRITES, COLOURS
from moving_entity import MovingEntity


class Player(MovingEntity):

    def __init__(self, game_ref):

        if type(game_ref) is not game.Game:
            raise TypeError("invalid reference")

        super().__init__(game_ref, PLAYER_SPRITES, PLAYER_SETTINS, "down_standing")

        self.lives = PLAYER_SETTINS["lives"]
        self.score = 0

        # If hand sanitizer is picked up
        self.boosted = False
        self.vulnerable = True
        self.threads = []

        self.animation_toggle = 2

    def update(self):

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                self.switch_directions(e.key)
                if e.key == pygame.K_ESCAPE:
                    self.game_ref.state = "pause"

        self.update_status()
        self.move()
        self.redraw()

    def update_status(self):
        font = pygame.font.Font('freesansbold.ttf', 50)

        text_surface, text_rect = self.text_objects('Pandemic Run', font, color=COLOURS["red"])
        text_rect.center = ((GAME_SETTINGS["width"] / 2), 30)
        self.game_ref.window.blit(text_surface, text_rect)

        text_surface_lives, text_rect_lives = self.text_objects("Lives:", font, color=COLOURS["red"])
        text_rect_lives.center = ((GAME_SETTINGS["width"] / 5) * 4, 30)
        self.game_ref.window.blit(text_surface_lives, text_rect_lives)

        text_surface_scores, text_rect_scores = self.text_objects(str(self.score), font, color=COLOURS["red"])
        text_rect_scores.center = ((GAME_SETTINGS["width"] / 5), 30)
        self.game_ref.window.blit(text_surface_scores, text_rect_scores)

    @staticmethod
    def text_objects(text, font, color=COLOURS["white"]):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

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
            self.game_ref.create_sanitizer_icon()
            for thread in self.threads:
                if thread.is_alive():
                    thread.cancel()
            t = threading.Timer(PLAYER_SETTINS["boosted_duration"], self.back_to_normal)
            self.threads.append(t)
            self.threads[-1].start()

    def check_virus(self):
        item_hit_list = pygame.sprite.spritecollide(self, self.game_ref.virus_list, False)
        if not self.boosted and len(item_hit_list) != 0 and self.vulnerable:
            self.vulnerable = False
            self.loose_life()
            if self.lives > 0:
                heart = self.game_ref.heart_list[-1]
                self.game_ref.all_sprite_list.remove(heart)
                self.game_ref.heart_list.remove(heart)
            t = threading.Timer(PLAYER_SETTINS["invincible_duration"], self.back_to_vulnerable)
            t.start()
        if self.boosted:
            for virus in item_hit_list:
                self.game_ref.virus_list.remove(virus)
                self.game_ref.all_sprite_list.remove(virus)

    def loose_life(self):
        if self.lives == 1:
            self.game_ref.state = "game_over"
        self.lives -= 1
        print(f"Lives: {self.lives}")

    def back_to_vulnerable(self):
        self.vulnerable = True

    def back_to_normal(self):
        print("-------------------------")
        print(f"{self.threads}")
        print("-------------------------")
        self.game_ref.all_sprite_list.remove(self.game_ref.sanitizer_icon)
        self.boosted = False

    def redraw(self):
        self.animate()
        self.game_ref.window.blit(self.image, (self.rect.x, self.rect.y))

    def animate(self):

        standing =  [1,4, 7,10,  13,16, 19,22, 25,28]
        one =       [2,3, 8,9,   14,15, 20,21, 26,27]
        two =       [5,6, 11,12, 17,18, 23,24, 29,30]

        dir_str = ""
        frame_count = self.game_ref.frame_count
        for direction in self.directions:
            if self.directions[direction]:
                dir_str = direction

        if dir_str == "":
            # print("returning")
            return

        if not self.is_valid_direction(dir_str):
            self.animation_toggle = 2
        elif frame_count in standing:
            self.animation_toggle = 2
        elif frame_count in two:
            self.animation_toggle = 3
        elif frame_count in one:
            self.animation_toggle = 1
        
        #elif frame_count % 30 == 0:
        #    self.animation_toggle = 3
        #elif frame_count % 20 == 0:
        #    self.animation_toggle = 2
        #elif frame_count % 15 == 0:
        #    self.animation_toggle = 1
        #elif frame_count % 5 == 0:
        #    self.animation_toggle = 2

        convert = {
            1: dir_str + "_1",
            2: dir_str + "_standing",
            3: dir_str + "_2",
        }

        dir_str = convert[self.animation_toggle]

        self.image = self.sprite_setting[dir_str].convert_alpha()
