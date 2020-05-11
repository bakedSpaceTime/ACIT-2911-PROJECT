import pygame
from text_box import TextBox
from button import Button
from settings import GAME_SETTINGS
from tkinter import messagebox, Tk
import webbrowser
from send_score import send_score


class EndMenu():

    def __init__(self, game_ref):
        self.game_ref = game_ref
        self.header_font = pygame.font.Font('freesansbold.ttf', 60)
        self.info_font = pygame.font.Font('freesansbold.ttf', 30)
        self.name_input = TextBox(500, 500, 200, 50, 12, 20)
        self.submit_button = Button(550, 550, 100, 50, 'Submit', (25,25,166), (255,255,255), 20)
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.name_input.add_text(event.key)
                if event.key == pygame.K_ESCAPE:
                    self.game_ref.state = "game"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.submit_button.clicked(mx, my) and self.name_input.return_text():
                        # pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                        self.submit_score()
        self.draw()

    def draw(self):
        text_surface, text_rect = self.text_objects('Your score is 0.', self.info_font, (255,255,0))
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 2))
        self.game_ref.window.blit(text_surface, text_rect)

        text_surface, text_rect = self.text_objects('Enter your name:', self.info_font)
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 1.5))
        self.game_ref.window.blit(text_surface, text_rect)

        text_surface, text_rect = self.text_objects('Game Over', self.header_font)
        text_rect.center = ((GAME_SETTINGS["width"] / 2), (GAME_SETTINGS["height"] / 4))
        self.game_ref.window.blit(text_surface, text_rect)

        self.submit_button.draw(self.game_ref.window)
        self.name_input.draw(self.game_ref.window)
        # self.clock.tick(30)
        # pygame.display.update()

    def text_objects(self, text, font, color=(255, 255, 255)):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def submit_score(self):
        try:
            r = send_score(self.name_input.return_text(), 500)
            webbrowser.open('http://rocky-river-43342.herokuapp.com/')
            # pygame.quit()
            # quit()
        except Exception as e:
            print(e)
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Could not connect to server')
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
