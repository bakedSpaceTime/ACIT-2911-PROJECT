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