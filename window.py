import pygame


WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Reversi')


class Window:
    def display():
        WIN.fill((255, 255, 255))
        pygame.display.update()
