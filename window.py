import pygame
import os


class Window:

    WIN = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)
    pygame.display.set_caption('Reversi')

    def width():
        return pygame.display.get_window_size()[0]

    def height():
        return pygame.display.get_window_size()[1]

    def background():
        background = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'background.png')),
            (Window.width(), Window.height())
            )
        Window.WIN.blit((background), (0, 0))
