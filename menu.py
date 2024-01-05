import pygame
from window import Window


WHITE = (255, 255, 255)
WELCOME = 'Welcome to reversi'
SELECT = 'Please select mode you want to play'
BUTTON_1 = 'Player vs Player'
BUTTON_2 = 'Player vs Computer'
BUTTON_3 = 'Computer vs Computer'


class Menu(Window):
    """
    Menu class displays menu window.
    """

    def __init__(self):

        pygame.font.init()
        self.window = Window()

        select_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/14))

        self.select_text = select_font.render(SELECT, 1, WHITE)

        self.multiplayer = self.multi_rect()
        self.solo = self.solo_rect()
        self.computer = self.computer_rect()

    def welcome_text(self):
        welcome_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/5))
        return welcome_font.render(WELCOME, 1, WHITE)

    def middle(self, text):
        # centers the text
        return ((self.window.width - text.get_width())/2)

    def button_text(self, text):
        # initializes button font and text
        button_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/10))

        return button_font.render(text, 1, WHITE)

    def button_width(self, button):
        # return button width
        return self.button_text(button).get_width()

    def button_height(self, button):
        # return button height
        return self.button_text(button).get_height()

    # creates rectangle, needed because of different window size ↓
    def multi_rect(self):
        # player vs player
        return pygame.Rect(
            self.middle(self.button_text(BUTTON_1)),
            self.header + self.space_btw_buttons,
            self.button_width(BUTTON_1),
            self.button_height(BUTTON_1))

    def solo_rect(self):
        # player vs computer
        return pygame.Rect(
            self.middle(self.button_text(BUTTON_2)),
            self.header + 2*self.space_btw_buttons
            + self.button_height(BUTTON_1),
            self.button_width(BUTTON_2),
            self.button_height(BUTTON_2))

    def computer_rect(self):
        # computer vs computer
        return pygame.Rect(
            self.middle(self.button_text(BUTTON_3)),
            # I can multiply button height times 2,
            # because they all have the same font
            self.header + 3*self.space_btw_buttons
            + 2*self.button_height(BUTTON_1),
            self.button_width(BUTTON_3),
            self.button_height(BUTTON_3))
    # ↑

    @property
    def welcome_height(self):
        return self.welcome_text().get_height()

    @property
    def select_height(self):
        return self.select_text.get_height()

    @property
    def header(self):
        return self.window.height/13 + self.welcome_height + self.select_height

    @property
    def space_btw_buttons(self):
        return (self.window.height - self.header
                - 3*self.button_height(BUTTON_1))/4

    def display(self):

        self.window.display()

        # displaying welcome text
        self.window.WIN.blit(
            self.welcome_text(),
            (self.middle(self.welcome_text()), self.window.height/13))

        # displaying select text
        self.window.WIN.blit(
            self.select_text,
            (
                self.middle(self.select_text),
                self.window.height/13 + self.welcome_height
                + self.window.height/60))

        # updating rectangle size
        multiplayer = self.multi_rect()
        self.multiplayer.update(multiplayer)
        # displaying button
        self.window.WIN.blit(
            self.button_text(BUTTON_1),
            (self.multiplayer.x, self.multiplayer.y))

        # updating rectangle size
        solo = self.solo_rect()
        self.solo.update(solo)
        # displaying button
        self.window.WIN.blit(
            self.button_text(BUTTON_2),
            (self.solo.x, self.solo.y))

        # updating rectangle size
        computer = self.computer_rect()
        self.computer.update(computer)
        # displaying button
        self.window.WIN.blit(
            self.button_text(BUTTON_3),
            (self.computer.x, self.computer.y))
