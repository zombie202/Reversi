import pygame
import os


class Window:

    WIN = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)
    pygame.display.set_caption('Reversi')

    def display():
        width, height = pygame.display.get_window_size()
        background = pygame.transform.scale(pygame.image.load(
            os.path.join('assets', 'tlo_wieksze.png')), (width, height))
        Window.WIN.blit((background), (0, 0))

        pygame.display.update()
