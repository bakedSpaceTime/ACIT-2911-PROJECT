import pygame
from settings import GAME_SETTINGS

class Game():
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode((GAME_SETTINGS['width'], GAME_SETTINGS['height']))
        self.x = 225
        self.y = 225
        self.width = 32
        self.height = 32
        self.velocity = 10
        self.directions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

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
        if self.directions["left"]:
            self.window.blit(self.charLeft, (self.x,self.y))
        elif self.directions["right"]:
            self.window.blit(self.charRight, (self.x,self.y))
        elif self.directions["up"]:
            self.window.blit(self.charUp, (self.x,self.y))
        elif self.directions["down"]:
            self.window.blit(self.charDown, (self.x, self.y))
        pygame.display.update()
        pygame.display.set_caption("Pandemic Run")

    def is_in_bounds(self, side: str):
        boundries = {
            "left": self.x > 0 + self.velocity,
            "right": self.x < GAME_SETTINGS['width'] - self.width - self.velocity,
            "up": self.y > 0 + self.velocity,
            "down": self.y < GAME_SETTINGS['height'] - self.height - self.velocity,
        }

        if side not in boundries.keys():
            raise ValueError("Valid bountries are 'left', 'right', 'up', 'down'.")

        return boundries[side]

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

    def move_player(self):

        if self.directions["left"] and self.is_in_bounds("left"):
            self.x -= self.velocity
        elif self.directions["right"] and self.is_in_bounds("right"):
            self.x += self.velocity
        elif self.directions["up"] and self.is_in_bounds("up"):
            self.y -= self.velocity
        elif self.directions["down"] and self.is_in_bounds("down"):
            self.y += self.velocity
  
    def main_game(self):
        while True:
            self.clock.tick(30)
            # pygame.time.delay(50)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                if e.type == pygame.KEYDOWN:
                    self.switch_directions(e.key)

            self.move_player()
            
            # print(self.x,self.y)
            self.redraw()


# if __name__ == "__main__":
#     main_game()
#     pygame.quit()