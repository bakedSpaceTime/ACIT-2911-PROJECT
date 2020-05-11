import pygame
# from text_box import TextBox
from button import Button
from settings import GAME_SETTINGS
# from tkinter import messagebox, Tk
import webbrowser
# from send_score import send_score


class StartMenu():

    def __init__(self, game_ref):
        self.game_ref = game_ref
        self.header_font = pygame.font.Font('freesansbold.ttf', 70)
        self.option_font = pygame.font.Font('freesansbold.ttf', 45)
        # self.name_input = TextBox(500, 500, 200, 50, 12, 20)
        # self.submit_button = Button(550, 550, 100, 50, 'Submit', (25,25,166), (255,255,255), 20)
        self.game_button = Button(550, 345, 120, 50, 'Start Game', (0,0,0), (255,255,0), 45)
        self.leaderboard_button = Button(550, 445, 120, 50, 'Leaderboard', (0,0,0), (255,255,0), 45)
        self.exit_button = Button(550, 545, 120, 60, 'Exit', (255,255,255), (0,0,0), 45)
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                pass
                # if event.key == pygame.K_ESCAPE:
                #     self.game_ref.state = "game"
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
        text_surface, text_rect = self.text_objects('Pandemic Run', self.header_font, color=(255,0,0))
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 4))
        self.game_ref.window.blit(text_surface, text_rect)

        self.game_button.draw(self.game_ref.window)
        self.leaderboard_button.draw(self.game_ref.window)
        self.exit_button.draw(self.game_ref.window)

    def text_objects(self, text, font, color=(255, 255, 255)):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
