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
from button import Button
from settings import GAME_SETTINGS, COLOURS
import webbrowser


class StartMenu():

    def __init__(self, game_ref):
        self.game_ref = game_ref
        self.header_font = pygame.font.Font('freesansbold.ttf', 70)
        self.option_font = pygame.font.Font('freesansbold.ttf', 45)
        self.game_button = Button(550, 345, 120, 50, 'Start Game', COLOURS["black"], COLOURS["yellow"], 45)
        self.leaderboard_button = Button(550, 445, 120, 50, 'Leaderboard', COLOURS["black"], COLOURS["yellow"], 45)
        self.exit_button = Button(550, 545, 120, 60, 'Exit', COLOURS["white"], COLOURS["black"], 45)
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.game_button.clicked(mx, my):
                    self.game_ref.state = "game"
                elif self.leaderboard_button.clicked(mx, my):
                    webbrowser.open('http://rocky-river-43342.herokuapp.com/')  
                elif self.exit_button.clicked(mx, my):
                    pygame.quit()
                    exit()
                    
        self.draw()

    def draw(self):
        text_surface, text_rect = self.text_objects('Pandemic Run', self.header_font, color=COLOURS["red"])
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 4))
        self.game_ref.window.blit(text_surface, text_rect)

        self.game_button.draw(self.game_ref.window)
        self.leaderboard_button.draw(self.game_ref.window)
        self.exit_button.draw(self.game_ref.window)

    def text_objects(self, text, font, color=COLOURS["white"]):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
