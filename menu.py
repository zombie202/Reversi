import pygame
from window import Window
pygame.font.init()


WHITE = (255, 255, 255)
WELCOME = 'Welcome to reversi'
SELECT = 'Please select mode you want to play'
BUTON_1 = 'Player vs Player'
BUTON_2 = 'Player vs Computer'
BUTON_3 = 'Computer vs Computer'


class Menu:

    def middle(text):
        return ((Window.width() - text.get_width())/2)

    def display():

        height = Window.height()

        welcome_font = pygame.font.SysFont('comicsans', int(height/6))
        welcome_text = welcome_font.render(WELCOME, 1, WHITE)
        welcome_height = welcome_text.get_height()

        select_font = pygame.font.SysFont('comicsans', int(height/14))
        select_text = select_font.render(SELECT, 1, WHITE)
        select_height = select_text.get_height()

        header = height/13 + welcome_height + select_height

        buton_font = pygame.font.SysFont('comicsans', int(height/14))
        buton_1_text = buton_font.render(BUTON_1, 1, WHITE)
        buton_2_text = buton_font.render(BUTON_2, 1, WHITE)
        buton_3_text = buton_font.render(BUTON_3, 1, WHITE)
        buton_width = buton_1_text.get_width()
        buton_height = buton_1_text.get_height()

        space_betwen_butons = (height - header - 3*buton_height)/4

        # player vs player
        multiplayer = pygame.Rect(
            Menu.middle(buton_1_text),
            header + space_betwen_butons,
            buton_width,
            buton_height
            )
        # player vs computer
        solo = pygame.Rect(
            Menu.middle(buton_2_text),
            header + 2*space_betwen_butons + buton_height,
            buton_width,
            buton_height
            )
        # computer vs computer
        computer = pygame.Rect(
            Menu.middle(buton_3_text),
            header + 3*space_betwen_butons + 2*buton_height,
            buton_width,
            buton_height
            )

        Window.background()
        Window.WIN.blit(welcome_text, (Menu.middle(welcome_text), height/13))
        Window.WIN.blit(
            select_text,
            (Menu.middle(select_text), height/13 + welcome_height)
            )
        Window.WIN.blit(buton_1_text, (multiplayer.x, multiplayer.y))
        Window.WIN.blit(buton_2_text, (solo.x, solo.y))
        Window.WIN.blit(buton_3_text, (computer.x, computer.y))

        pygame.display.update()
