import pygame
import os


class Window:
    """
    Initializes window, display background image, return width
    and height of the window
    """
    def __init__(self, width=1200, height=700):
        pygame.init()
        pygame.display.set_caption('Reversi')
        # initialize window
        self.WIN = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.image = pygame.image.load(
            os.path.join('assets', 'background.png'))

    @property
    def width(self):
        """returns window width"""
        return pygame.display.get_window_size()[0]

    @property
    def height(self):
        """returns window height"""
        return pygame.display.get_window_size()[1]

    def display(self):
        background = pygame.transform.scale(
            self.image,
            (self.width, self.height))

        # display backgronud
        self.WIN.blit((background), (0, 0))
