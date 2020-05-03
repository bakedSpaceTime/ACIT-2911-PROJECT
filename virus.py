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
from settings import GAME_SETTINGS, VIRUS_SETTINS, VIRUS_SPRITES, VIRUS_SPAWN_POINTS
from moving_entity import MovingEntity


class Virus(MovingEntity):
    def __init__(self, game_ref, virus_num):

        if type(game_ref) is not game.Game:
            raise TypeError("invalid reference")

        super().__init__(game_ref, VIRUS_SPRITES, VIRUS_SETTINS, "right")
        
        #### These lines not needed once proper sprites are used
        self.image = pygame.transform.scale(self.image, (27,27))
        self.rect = self.image.get_rect()
        #################

        self.rect.x = VIRUS_SPAWN_POINTS[virus_num][0]
        self.rect.y = VIRUS_SPAWN_POINTS[virus_num][1]
        # set default direction
        self.directions["right"] = True

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        self.move()
        self.redraw()

    def move(self):
        self.switch_directions()
        if self.is_valid_direction("left"):
            self.rect.x -= self.velocity
        elif self.is_valid_direction("right"):
            self.rect.x += self.velocity
    
    def switch_directions(self):
        # Basic Behavior
        # Not sure how we want it to behave
        
        if self.will_hit_wall("left"):
            self.directions["left"] = False
            self.directions["right"] = True
        elif self.will_hit_wall("right"):
            self.directions["right"] = False
            self.directions["left"] = True
            
