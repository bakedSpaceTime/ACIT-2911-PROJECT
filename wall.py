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
from math import ceil
from os.path import join as path_join
from settings import OTHER_SPRITES


# class Wall():

#     def __init__(self, x, y, width, height):

#         temp_image = pygame.image.load(path_join('images','Shelf', 'Front.png'))
#         temp_image_rect = temp_image.get_rect()
        
#         self.num_width = ceil(width / temp_image_rect.width)
#         self.num_height = ceil(height / temp_image_rect.height)
#         print(self.num_width, self.num_height, "num width, height")

#         self.shelf_list = pygame.sprite.Group()

#         for i in range(self.num_width):
#             for j in range(self.num_height):
#                 new_shelf = Shelf(i * temp_image_rect.height + x, j * temp_image_rect.height + y)
#                 self.shelf_list.add(new_shelf)

#         self.rect = pygame.Rect(x, y, width, height)
#         print(self.rect, "wall rect")
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, type = 'wall'):
        super().__init__()
        self.image = OTHER_SPRITES[type]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
