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
        while run:
            clock.tick(60)
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # check if player want to close the window
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # checks which mode player selected
                    # and proced to display board size window
                    if self.menu.multiplayer.collidepoint(mouse_pos):
                        # game_mode = 'multi'
                        menu_running = False
                        board_running = True
                    if self.menu.solo.collidepoint(mouse_pos):
                        # game_mode = 'solo'
                        menu_running = False
                        board_running = True
                    if self.menu.computer.collidepoint(mouse_pos):
                        # game_mode = 'computer'
                        menu_running = False
                        board_running = True
                    # checks if player wnt to continue or go back to menu
                    # and proced to display game window
                    if self.board_size.back_button.collidepoint(mouse_pos):
                        board_running = False
                        menu_running = True
                    if self.board_size.continue_button.collidepoint(mouse_pos):
                        board_running = False
                        game_running = True

                for box in self.board_size.input_box:
                    box.handle_events(event, 8, 30)

            if menu_running:
                self.menu.display()
            if board_running:
                self.board_size.display()
            if game_running:
                pass

        pygame.quit()


def main():
    game = Engine()
    game.run()
