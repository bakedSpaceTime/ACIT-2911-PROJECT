import pygame
from button import Button
from settings import GAME_SETTINGS
import webbrowser


class PauseMenu():
    def __init__(self, game_ref):
        self.game_ref = game_ref
        self.header_font = pygame.font.Font('freesansbold.ttf', 70)
        self.option_font = pygame.font.Font('freesansbold.ttf', 45)
        self.game_button = Button(550, 345, 120, 50, 'Resume Game', (0,0,0), (255,255,0), 45)
        self.restart_button = Button(550, 445, 120, 50, 'Restart Game', (0,0,0), (255,255,0), 45)
        self.exit_button = Button(450, 545, 330, 60, 'End Game', (255,255,255), (0,0,0), 45)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_ref.state = "game"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.game_button.clicked(mx, my):
                    self.game_ref.state = "game"
                elif self.restart_button.clicked(mx, my):
                    pass
                elif self.exit_button.clicked(mx, my):
                    self.game_ref.state = "game_over"
                    
        self.draw()

    def draw(self):
        text_surface, text_rect = self.text_objects('Paused', self.header_font, color=(255,0,0))
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 4))
        self.game_ref.window.blit(text_surface, text_rect)

        self.game_button.draw(self.game_ref.window)
        self.restart_button.draw(self.game_ref.window)
        self.exit_button.draw(self.game_ref.window)

    def text_objects(self, text, font, color=(255, 255, 255)):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
