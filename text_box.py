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
vec = pygame.math.Vector2


class TextBox:
    """ Input Textbox Class """
    def __init__(self, x, y, width, height, max_length, font_size=20):
        """ Textbox Class """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = vec(x, y)
        self.size = vec(width, height)
        self.image = pygame.Surface((width, height))
        self.text = ''
        self.font = pygame.font.Font('freesansbold.ttf', font_size)
        self.bg_color = (0, 0, 0)
        # self.bg_color = (255, 255, 255)
        self.special = [8, 32, 127]
        self.max_length = max_length

    def draw(self, window):
        """ Displays itself on the window """
        self.image.fill(self.bg_color)
        text = self.font.render(self.text, True, (255, 255, 255))
        font_height = text.get_height()
        font_width = text.get_width()
        self.image.blit(text, ((self.width - font_width) // 2, (self.height - font_height) // 2))
        window.blit(self.image, self.position)

    def add_text(self, key):
        """ Converts keys to characters and adds it to the text """
        try:
            if self.within_length() and ((65 <= key <= 90) or (97 <= key <= 122)):
                text = list(self.text)
                text.append(chr(key))
                self.text = "".join(text).upper()
                print(self.text)
            elif key == 32 and self.within_length():
                text = list(self.text)
                text.append(' ')
                self.text = "".join(text)
            elif key == 8:
                text = list(self.text)
                text.pop()
                self.text = "".join(text)
            else:
                print(key)
        except:
            print(key)

    def within_length(self):
        """ Checks if there is room for more text """
        if len(self.text) < self.max_length:
            return True
        return False

    def return_text(self):
        """ Returns the text in the Textbox """
        return self.text
