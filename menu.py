import pygame
from window import Window
pygame.font.init()


WHITE = (255, 255, 255)
WELCOME = 'Welcome to reversi'
SELECT = 'Please select mode you want to play'
BUTTON_1 = 'Player vs Player'
BUTTON_2 = 'Player vs Computer'
BUTTON_3 = 'Computer vs Computer'


class Menu(Window):

    def __init__(self):

        self.window = Window()

        welcome_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/5))

        self.welcome_text = welcome_font.render(WELCOME, 1, WHITE)

        select_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/14))

        self.select_text = select_font.render(SELECT, 1, WHITE)

        # player vs player
        self.multiplayer = self.multi_rect()

        # player vs computer
        self.solo = self.solo_rect()

        # computer vs computer
        self.computer = self.computer_rect()

    def middle(self, text):
        return ((self.window.width - text.get_width())/2)

    def button_text(self, text):
        button_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/10))

        return button_font.render(text, 1, WHITE)

    def button_width(self, button):
        return self.button_text(button).get_width()

    def button_height(self, button):
        return self.button_text(button).get_height()

    def multi_rect(self):
        return pygame.Rect(
            self.middle(self.button_text(BUTTON_1)),
            self.header + self.space_btw_buttons,
            self.button_width(BUTTON_1),
            self.button_height(BUTTON_1))

    def solo_rect(self):
        return pygame.Rect(
            self.middle(self.button_text(BUTTON_2)),
            self.header + 2*self.space_btw_buttons + self.button_height(BUTTON_1),
            self.button_width(BUTTON_2),
            self.button_height(BUTTON_2))

    def computer_rect(self):
        return pygame.Rect(
            self.middle(self.button_text(BUTTON_3)),
            self.header + 3*self.space_btw_buttons + 2*self.button_height(BUTTON_1),  # I can multiply button height times 2, because they all have the same font
            self.button_width(BUTTON_3),
            self.button_height(BUTTON_3))

    @property
    def welcome_height(self):
        return self.welcome_text.get_height()

    @property
    def select_height(self):
        return self.select_text.get_height()

    @property
    def header(self):
        return self.window.height/13 + self.welcome_height + self.select_height

    @property
    def space_btw_buttons(self):
        return (self.window.height - self.header - 3*self.button_height(BUTTON_1))/4

    def display(self):

        self.window.display()

        self.window.WIN.blit(
            self.welcome_text,
            (self.middle(self.welcome_text), self.window.height/13))

        self.window.WIN.blit(
            self.select_text,
            (
                self.middle(self.select_text),
                self.window.height/13 + self.welcome_height + self.window.height/60))

        multiplayer = self.multi_rect()
        self.multiplayer.update(multiplayer)
        self.window.WIN.blit(
            self.button_text(BUTTON_1),
            (self.multiplayer.x, self.multiplayer.y))

        solo = self.solo_rect()
        self.solo.update(solo)
        self.window.WIN.blit(
            self.button_text(BUTTON_2),
            (self.solo.x, self.solo.y))

        computer = self.computer_rect()
        self.computer.update(computer)
        self.window.WIN.blit(
            self.button_text(BUTTON_3),
            (self.computer.x, self.computer.y))

        pygame.display.update()

    def running(self, game_mode, menu_running, board_running):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        if self.multiplayer.collidepoint(mouse_pos) and mouse_clicked:
            pass
        if self.solo.collidepoint(mouse_pos) and mouse_clicked:
            pass
        if self.computer.collidepoint(mouse_pos) and mouse_clicked:
            pass

