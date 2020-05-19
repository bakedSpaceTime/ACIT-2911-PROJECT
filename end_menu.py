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
from text_box import TextBox
from button import Button
from settings import GAME_SETTINGS, COLOURS
from tkinter import messagebox, Tk
import webbrowser
from send_score import send_score


class EndMenu():
    """ EndMenu class """

    def __init__(self, game_ref):
        """ Initialize EndMenu class """
        self.game_ref = game_ref
        self.header_font = pygame.font.Font('freesansbold.ttf', 60)
        self.info_font = pygame.font.Font('freesansbold.ttf', 30)
        self.name_input = TextBox(500, 550, 200, 50, 12, 20)
        self.submit_button = Button(550, 610, 100, 50, 'Submit', COLOURS["blue"], COLOURS["white"], 20)
        self.start_button = Button(550, 710, 100, 50, 'Exit', COLOURS["blue"], COLOURS["white"], 20)

    def update(self):
        """ Keep the game running """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.name_input.add_text(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.submit_button.clicked(mx, my) and self.name_input.return_text():
                        self.submit_score()
                        self.game_ref.state = "start"
                elif self.start_button.clicked(mx, my):
                    self.game_ref.state = "start"
        self.draw()

    def draw(self):
        """ Output score, input for name, submit, and exit button"""
        score = self.game_ref.player.score
        text_surface, text_rect = self.text_objects(f'Your score is {score}', self.info_font, color=COLOURS["yellow"])
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 2))
        self.game_ref.window.blit(text_surface, text_rect)

        text_surface, text_rect = self.text_objects('Enter your name:', self.info_font)
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 1.5))
        self.game_ref.window.blit(text_surface, text_rect)

        text_surface, text_rect = self.text_objects('Game Over', self.header_font)
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 4))
        self.game_ref.window.blit(text_surface, text_rect)

        self.submit_button.draw(self.game_ref.window)
        self.start_button.draw(self.game_ref.window)
        self.name_input.draw(self.game_ref.window)

    def text_objects(self, text, font, color=COLOURS["white"]):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def submit_score(self):
        """ Post score and name to the website """
        try:
            score = self.game_ref.player.score
            r = send_score(self.name_input.return_text(), score)
            webbrowser.open('http://rocky-river-43342.herokuapp.com/')
            self.game_ref.state = "start"
        except Exception as e:
            print(e)
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Could not connect to server')
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
