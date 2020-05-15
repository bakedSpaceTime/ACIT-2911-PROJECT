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
from settings import OTHER_SPRITES
WHITE = (255, 255, 255)


class ToiletPaper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = OTHER_SPRITES['toilet_paper']
        # pygame.Surface([15, 15])
        # self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class HandSanitizer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = OTHER_SPRITES['hand_sanitizer']

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
