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
from settings import GAME_SETTINGS
from wall import Wall

white = (255, 255, 255)
black = (0, 0, 0)


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((GAME_SETTINGS['width'], GAME_SETTINGS['height']))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Pandemic Run")
        # self.game_intro()
        self.window.fill((0, 0, 0))

        pygame.mixer.music.load('audio/bg.mp3')
        pygame.mixer.music.play(-1)
        self.effect = pygame.mixer.Sound('audio/Ghost.wav')
        self.char = pygame.image.load('images/pac-up.bmp')
        self.charRight = pygame.image.load('images/pac-right.bmp')
        self.charLeft = pygame.image.load('images/pac-left.bmp')
        self.charUp = pygame.image.load('images/pac-up.bmp')
        self.charDown = pygame.image.load('images/pac-down.bmp')

        self.x = 225
        self.y = 225
        self.width = 32
        self.height = 32
        self.velocity = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.all_sprite_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()

        wall = Wall(0, 0, 10, 500)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(0, 490, 500, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(490, 0, 10, 500)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(0, 0, 500, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(450, 450, 400, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(50, 100, 400, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        wall = Wall(50, 100, 10, 400)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)

        self.player = pygame.sprite.Sprite()
        self.player.image = pygame.Surface([32,32])
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = self.x
        self.player.rect.y = self.y
        # self.main_game()

    def game_intro(self):
       pass
    
    def move(self, player, velocity_x, velocity_y, wall_list):
        played = False
        player.rect.x += velocity_x
        block_hit_list = pygame.sprite.spritecollide(player, wall_list, False)
        for block in block_hit_list:
            if velocity_x > 0:
                player.rect.right = block.rect.left
            else:
                player.rect.left = block.rect.right
            # self.effect.play()
            played = True

        player.rect.y += velocity_y
        block_hit_list = pygame.sprite.spritecollide(player, wall_list, False)
        for block in block_hit_list:
            if velocity_y > 0:
                player.rect.bottom = block.rect.top
            else:
                player.rect.top = block.rect.bottom
            # if not played:
                # self.effect.play()

    def main_game(self):
        while True:
            self.clock.tick(30)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.move(self.player, -self.velocity, 0, self.wall_list)

                self.left = True
                self.right = False
                self.up = False
                self.down = False
            elif keys[pygame.K_RIGHT]:
                self.move(self.player, self.velocity, 0, self.wall_list)
                self.right = True
                self.left = False
                self.up = False
                self.down = False
            elif keys[pygame.K_UP]:
                self.move(self.player, 0, -self.velocity, self.wall_list)
                self.right = False
                self.left = False
                self.up = True
                self.down = False
            elif keys[pygame.K_DOWN]:
                self.move(self.player, 0, self.velocity, self.wall_list)
                self.right = False
                self.left = False
                self.up = False
                self.down = True
            else:
                if self.right:
                    self.move(self.player, self.velocity, 0, self.wall_list)
                elif self.left:
                    self.move(self.player, -self.velocity, 0, self.wall_list)
                elif self.up:
                    self.move(self.player, 0, -self.velocity, self.wall_list)
                elif self.down:
                    self.move(self.player, 0, self.velocity, self.wall_list)
            self.all_sprite_list.update()
            self.window.fill((0, 0, 0))
            self.all_sprite_list.draw(self.window)

            if self.left:
                self.window.blit(self.charLeft, (self.player.rect.x, self.player.rect.y))
            elif self.right:
                self.window.blit(self.charRight, (self.player.rect.x, self.player.rect.y))
            elif self.up:
                self.window.blit(self.charUp, (self.player.rect.x, self.player.rect.y))
            elif self.down:
                self.window.blit(self.charDown, (self.player.rect.x, self.player.rect.y))
            pygame.display.update()
