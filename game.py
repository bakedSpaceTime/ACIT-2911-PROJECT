import pygame


def redraw():
    window.fill((0, 0, 0))
    # window.blit(bg, (0,0))
    if left:
        window.blit(charLeft, (x,y))
    elif right:
        window.blit(charRight, (x,y))
    elif up:
        window.blit(charUp, (x,y))
    elif down:
        window.blit(charDown, (x, y))
    # else:
    #     window.blit(charDown, (x, y))
    pygame.display.update()

# def main_game():
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Maze")

bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/pac-up.bmp')
charRight = pygame.image.load('images/pac-right.bmp')
charLeft = pygame.image.load('images/pac-left.bmp')
charUp = pygame.image.load('images/pac-up.bmp')
charDown = pygame.image.load('images/pac-down.bmp')

clock = pygame.time.Clock()

x = 225
y = 225
width = 32
height = 32
velocity = 10
left = False
right = False
up = False
down = False


while True:
    clock.tick(30)
    # pygame.time.delay(50)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > 0 - velocity:
            x -= velocity
            left = True
            right = False
            up = False
            down = False
    elif keys[pygame.K_RIGHT]:
        if x < 500 - width - velocity:
            x += velocity
            right = True
            left = False
            up = False
            down = False
    elif keys[pygame.K_UP]:
        if y > 0:
            y -= velocity
            right = False
            left = False
            up = True
            down = False
    elif keys[pygame.K_DOWN]:
        if y < 500 - height:
            y += velocity
            right = False
            left = False
            up = False
            down = True
    else:
        if right:
            if x < 500 - width - velocity:
                x += velocity
        elif left:
            if x > 0 + velocity:
                x -= velocity
        elif up:
            if y > 0 + velocity:
                y -= velocity
        elif down:
            if y < 500 - height - velocity:
                y += velocity
    print(x,y)
    redraw()


# if __name__ == "__main__":
#     main_game()
#     pygame.quit()