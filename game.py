import pygame

class Game():
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode((500, 500))
        self.x = 225
        self.y = 225
        self.width = 32
        self.height = 32
        self.velocity = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        # self.bg = pygame.image.load('images/bg.jpg')
        self.char = pygame.image.load('images/pac-up.bmp')
        self.charRight = pygame.image.load('images/pac-right.bmp')
        self.charLeft = pygame.image.load('images/pac-left.bmp')
        self.charUp = pygame.image.load('images/pac-up.bmp')
        self.charDown = pygame.image.load('images/pac-down.bmp')

        self.clock = pygame.time.Clock()
        self.run = True

    def redraw(self):
        self.window.fill((0, 0, 0))
        # self.window.blit(bg, (0,0))
        if self.left:
            self.window.blit(self.charLeft, (self.x,self.y))
        elif self.right:
            self.window.blit(self.charRight, (self.x,self.y))
        elif self.up:
            self.window.blit(self.charUp, (self.x,self.y))
        elif self.down:
            self.window.blit(self.charDown, (self.x, self.y))
        pygame.display.update()
        pygame.display.set_caption("Pandemic Run")

    def main_game(self):
        while True:
            self.clock.tick(30)
            # pygame.time.delay(50)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                if self.x > 0 - self.velocity:
                    self.x -= self.velocity
                    self.left = True
                    self.right = False
                    self.up = False
                    self.down = False
            elif keys[pygame.K_RIGHT]:
                if self.x < 500 - self.width - self.velocity:
                    self.x += self.velocity
                    self.right = True
                    self.left = False
                    self.up = False
                    self.down = False
            elif keys[pygame.K_UP]:
                if self.y > 0:
                    self.y -= self.velocity
                    self.right = False
                    self.left = False
                    self.up = True
                    self.down = False
            elif keys[pygame.K_DOWN]:
                if self.y < 500 - self.height:
                    self.y += self.velocity
                    self.right = False
                    self.left = False
                    self.up = False
                    self.down = True
            else:
                if self.right:
                    if self.x < 500 - self.width - self.velocity:
                        self.x += self.velocity
                elif self.left:
                    if self.x > 0 + self.velocity:
                        self.x -= self.velocity
                elif self.up:
                    if self.y > 0 + self.velocity:
                        self.y -= self.velocity
                elif self.down:
                    if self.y < 500 - self.height - self.velocity:
                        self.y += self.velocity
            print(self.x,self.y)
            self.redraw()


# if __name__ == "__main__":
#     main_game()
#     pygame.quit()