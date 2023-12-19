import pygame
import os


class Window:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Reversi')
        self.WIN = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)
        self.image = pygame.image.load(
            os.path.join('assets', 'background.png'))

    @property
    def width(self):
        return pygame.display.get_window_size()[0]

    @property
    def height(self):
        return pygame.display.get_window_size()[1]

    def display(self):
        background = pygame.transform.scale(
            self.image,
            (self.width, self.height))

        self.WIN.blit((background), (0, 0))
