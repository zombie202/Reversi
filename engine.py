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
        self.board_size = BoardSize()
        self.restart()

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
                    if self.menu.solo.collidepoint(mouse_pos):
                        game_mode = 'solo'
                        self.menu_to_board()
                    if self.menu.computer.collidepoint(mouse_pos):
                        game_mode = 'computer'
                        self.menu_to_board()
                    # checks if player want to continue or go back to menu
                    # and proced to display game window
                    if self.board_size.back_button.collidepoint(mouse_pos):
                        self.board_to_menu()
                    if not self.game_running and self.board_size.next and \
                       self.board_size.continue_button.collidepoint(mouse_pos):
                        self.board_running = False
                        game = Game(
                            self.board_size.get_row_number(),
                            self.board_size.get_column_number(),
                            game_mode,
                            self.board_size.window.width,
                            self.board_size.window.height)
                        self.game_running = True

                if self.game_running:
                    game.get_mouse_input(event)

                if self.board_running:
                    for box in self.board_size.input_box:
                        box.handle_events(event, 8, 30)

            if self.menu_running:
                self.menu.display()
            if self.board_running:
                self.board_size.display()
            if self.game_running:
                game.display()
                game.game()

            if self.game_running and game.restart:
                self.restart()

            pygame.display.update()

        pygame.quit()

    def menu_to_board(self):
        """proceed to close menu and display board size"""
        self.menu_running = False
        self.board_running = True
        self.colapse_rect()

    def colapse_rect(self):
        """colapses menu rectangles"""
        nul = pygame.Rect(0, 0, 0, 0)
        self.menu.multiplayer.update(nul)
        self.menu.solo.update(nul)
        self.menu.computer.update(nul)

    def board_to_menu(self):
        """proceed to close board size and display menu"""
        self.board_running = False
        self.menu_running = True
        multiplayer = self.menu.multi_rect()
        solo = self.menu.multi_rect()
        computer = self.menu.computer_rect()
        self.menu.multiplayer.update(multiplayer)
        self.menu.solo.update(solo)
        self.menu.computer.update(computer)

    def restart(self):
        """restarts the game(goes back to main menu)"""
        self.menu_running = True
        self.board_running = False
        self.game_running = False


def main():
    """runs the game"""
    game = Engine()
    game.run()
