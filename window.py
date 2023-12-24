import pygame
import os


class Window:
    """
    Window class initializes window and displays backgroung image.
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Reversi')
        # initialize window
        self.WIN = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)
        self.image = pygame.image.load(
            os.path.join('assets', 'background.png'))

    @property
    def width(self):
        # returns window width
        return pygame.display.get_window_size()[0]

    @property
    def height(self):
        # returns window height
        return pygame.display.get_window_size()[1]

    def display(self):
        background = pygame.transform.scale(
            self.image,
            (self.width, self.height))

        # display backgronud
        self.WIN.blit((background), (0, 0))
