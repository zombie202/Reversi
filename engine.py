import pygame
from menu import Menu
from board_size import BoardSize
from game import Game


class Engine:
    """
    class operating main game loop, handling events
    and switching beetwen windows
    """
    def __init__(self):
        self.menu = Menu()
        # self.board_size = BoardSize()
        self.menu_running = True
        self.board_running = False
        self.game_running = False

    def run(self):
        """main game loop"""
        clock = pygame.time.Clock()
        run = True
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
                        game_mode = 'multi'
                        self.menu_to_board()
                        board_size = self.make_board_size()
                    if self.menu.solo.collidepoint(mouse_pos):
                        game_mode = 'solo'
                        self.menu_to_board()
                        board_size = self.make_board_size()
                    if self.menu.computer.collidepoint(mouse_pos):
                        game_mode = 'computer'
                        self.menu_to_board()
                        board_size = self.make_board_size()
                    # checks if player want to continue or go back to menu
                    # and proced to display game window
                    if board_size.back_button.collidepoint(mouse_pos):
                        self.board_running = False
                        self.menu_running = True
                    if not self.game_running and board_size.next and \
                       board_size.continue_button.collidepoint(mouse_pos):
                        self.board_running = False
                        game = Game(
                            board_size.get_row_number(),
                            board_size.get_column_number(),
                            game_mode,
                            board_size.window.width,
                            board_size.window.height)
                        self.game_running = True

                if self.game_running:
                    game.get_mouse_input(event)

                if self.board_running:
                    for box in board_size.input_box:
                        box.handle_events(event, 8, 30)

            if self.menu_running:
                self.menu.display()
            if self.board_running:
                board_size.display()
            if self.game_running:
                game.display()
                game.game()

            if self.game_running and game.restart:
                self.restart()

            pygame.display.update()

        pygame.quit()

    def menu_to_board(self):
        self.menu_running = False
        self.board_running = True

    def make_board_size(self):
        return BoardSize(
            self.menu.window.width,
            self.menu.window.height)

    # def colapse_rect(self):
    #     nul = pygame.Rect(0, 0, 0, 0)
    #     self.menu.multiplayer.update(nul)
    #     self.menu.solo.update(nul)
    #     self.menu.computer.update(nul)

    def restart(self):
        """restarts the game(goes back to main menu)"""
        self.__init__()


def main():
    """runs the game"""
    game = Engine()
    game.run()
