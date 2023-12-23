import pygame
from menu import Menu
from board_size import BoardSize


class Engine:

    def __init__(self):
        self.menu = Menu()
        self.board_size = BoardSize()

    def run(self):
        clock = pygame.time.Clock()
        run = True
        menu_running = True
        board_running = False
        game_running = False
        game_mode = str
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                for box in self.board_size.input_box:
                    box.handle_events(event, 8, 30)

            if menu_running:
                self.menu.display()
                self.menu.running(game_mode, menu_running, board_running)
            if board_running:
                self.board_size.display()
            if game_running:
                pass

        pygame.quit()


def main():
    game = Engine()
    game.run()
