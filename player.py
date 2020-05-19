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
from settings import GAME_SETTINGS, PLAYER_SETTINS, PLAYER_SPRITES, COLOURS
from moving_entity import MovingEntity


class Player(MovingEntity):
    """ Player class """

    def __init__(self, game_ref):
        """ Initialize Player class """

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
        """ Keep the game running """
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                self.switch_directions(e.key)
                if e.key == pygame.K_ESCAPE:
                    self.game_ref.state = "pause"
                    self.game_ref.time.pause()
                if e.key == pygame.K_a:
                    self.game_ref.toilet_list = pygame.sprite.Group()

        self.update_status()
        self.score_penalty()
        self.move()
        self.redraw()

    def score_penalty(self):
        """ Minus 1 score every 3 seconds """
        if self.game_ref.state != "pause":
            if int(self.game_ref.time.get_current()) % 3 == 0\
                    and int(self.game_ref.time.get_current()) != self.game_ref.time.previous:
                self.game_ref.time.previous = int(self.game_ref.time.get_current())
                # print(int(self.game_ref.time.get_current()))
                # - 1 score every 3 seconds
                if self.score > 0:
                    self.score -= 1

    def restart_position(self):
        """ Reset the the starting position """
        for direction, val in self.directions.items():
            self.directions[direction] = False
        self.image = self.sprite_setting["down_standing"]
        self.rect = self.image.get_rect()
        self.rect.x = self.entity_settings["starting_x"]
        self.rect.y = self.entity_settings["starting_y"]

    def update_status(self):
        """ Update the character status """
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
        """ Creates text on the screen """
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def move(self):
        """ Move the player """
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
        """ Determine where the player sprite will be facing """
        key_str = self.key_to_direction_str(key)
        if key_str in self.directions.keys():
            for direction in self.directions:
                if direction == key_str:
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False

    @staticmethod
    def key_to_direction_str(key):
        """ Converts a key press to a direction on the screen """
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
        """ Check if there is collision between player and toilet paper, hand sanitizer and virus"""
        self.collect_toilet_paper()
        self.collect_hand_sanitizer()
        self.check_virus()

    def collect_toilet_paper(self):
        """ Check if there is collision between player and toilet paper, +1 score if contact one """
        item_hit_list = pygame.sprite.spritecollide(self, self.game_ref.toilet_list, False)
        for toilet_paper in item_hit_list:
            self.game_ref.toilet_list.remove(toilet_paper)
            self.game_ref.all_sprite_list.remove(toilet_paper)
            self.score += 1

    def collect_hand_sanitizer(self):
        """ Check if there is collision between player and hand sanitizer, 5 second able to kill virus if contact one """
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
        """ Check if there is collision between player and virus, kills virus of collected hand sanitizer, -1 life if no """
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
        """ If life is reduced to 0, game over"""
        if self.lives == 1:
            self.game_ref.state = "game_over"
        self.lives -= 1
        print(f"Lives: {self.lives}")

    def back_to_vulnerable(self):
        """ Return back to vulnerable mode (normal mode) """
        self.vulnerable = True

    def back_to_normal(self):
        """ No longer can kill virus """
        print("-------------------------")
        print(f"{self.threads}")
        print("-------------------------")
        self.game_ref.all_sprite_list.remove(self.game_ref.sanitizer_icon)
        self.boosted = False

    def redraw(self):
        """ Redraw """
        self.animate()
        self.game_ref.window.blit(self.image, (self.rect.x, self.rect.y))

    def animate(self):
        """ Animate the character sprite movement """
        standing = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
        one = [2, 3, 8, 9, 14, 15, 20, 21, 26, 27]
        two = [5, 6, 11, 12, 17, 18, 23, 24, 29, 30]

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

        # elif frame_count % 30 == 0:
        #    self.animation_toggle = 3
        # elif frame_count % 20 == 0:
        #    self.animation_toggle = 2
        # elif frame_count % 15 == 0:
        #    self.animation_toggle = 1
        # elif frame_count % 5 == 0:
        #    self.animation_toggle = 2

        convert = {
            1: dir_str + "_1",
            2: dir_str + "_standing",
            3: dir_str + "_2",
        }

        dir_str = convert[self.animation_toggle]

        self.image = self.sprite_setting[dir_str].convert_alpha()
