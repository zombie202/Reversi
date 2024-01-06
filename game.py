import pygame
import os
from window import Window
from board import Board
from player import Player
from computer import Computer
pygame.font.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLACK_SCORE = 'BLACK:'
WHITE_SCORE = 'WHITE:'
BLACK_TURN = 'BLACK TURN'
WHITE_TURN = 'WHITE TURN'


class Game(Window, Board):
    """
    class used for handling turns and displaying the game
    """
    def __init__(self, row, column, mode, width, height):
        self.window = Window(width, height)
        self.board = Board(row, column)
        if mode == 'multi':
            self.player1 = Player(self.board, BLACK)
            self.player2 = Player(self.board, WHITE)
        elif mode == 'solo':
            self.player1 = Player(self.board, BLACK)
            self.player2 = Computer(self.board, WHITE)
        elif mode == 'computer':
            self.player1 = Computer(self.board, BLACK)
            self.player2 = Computer(self.board, WHITE)

        self.mode = mode

        self.cell_image = pygame.image.load(
            os.path.join('assets', 'cell.png'))
        self.white = pygame.image.load(
            os.path.join('assets', 'bialy_pionek.png'))
        self.black = pygame.image.load(
            os.path.join('assets', 'czarny_pionek.png'))

        self.board_rect = self.board_rectangle()
        self.black_score_rect = self.black_score_rectangle()
        self.white_score_rect = self.white_score_rectangle()
        self.turn_rect = self.turn_rectangle()
        self.cell = ()
        self.mouse_input = ()
        self.turn = BLACK
        self.empty = self.board.count_pieces()[2]
        self.restart = False

    def text(self, text):
        """renders text"""
        text_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/12))
        return text_font.render(text, 1, WHITE)

    def text_width(self, text):
        """return text width"""
        return self.text(text).get_width()

    def text_height(self, text):
        """returns text height"""
        return self.text(text).get_height()

    def board_rectangle(self):
        return pygame.Rect(
            (self.window.width - self.window.height - self.window.height/20)/2,
            self.window.height/40,
            self.window.height - self.window.height/20,
            self.window.height - self.window.height/20)

    """creates rectangle, needed because of different window size ↓"""
    def black_score_rectangle(self):
        return pygame.Rect(
            self.board_rect.right + 50,
            self.board_rect.top,
            self.text_width(BLACK_SCORE),
            self.text_height(BLACK_SCORE))

    def white_score_rectangle(self):
        return pygame.Rect(
            self.black_score_rect.left,
            self.black_score_rect.bottom + 10,
            self.text_width(WHITE_SCORE),
            self.text_height(WHITE_SCORE))

    def turn_rectangle(self):
        return pygame.Rect(
            self.white_score_rect.left,
            self.white_score_rect.bottom + 20,
            self.text_width(WHITE_TURN),
            self.text_height(WHITE_TURN))
    "↑"

    def get_mouse_input(self, event):
        """
        gets mouse position and checks if player clicked square,
        then calculates which square player clicked
        """
        rect = self.board_rectangle()
        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos_x > rect.right or \
               mouse_pos_x < rect.left or \
               mouse_pos_y > rect.bottom or \
               mouse_pos_y < rect.top:
                pass
            else:
                column = (mouse_pos_x - self.board_rect.left) // \
                    self.cell.get_width()
                row = (mouse_pos_y - self.board_rect.top) // \
                    self.cell.get_height()
                position = (row, column)
                self.mouse_input = position

    def displaying_board(self):
        """displays board"""
        board_rect = self.board_rectangle()
        self.board_rect.update(board_rect)
        if self.board.row > self.board.column:
            self.cell = pygame.transform.scale(
                self.cell_image,
                (
                    self.board_rect.width/self.board.row,
                    self.board_rect.height/self.board.row))
        else:
            self.cell = pygame.transform.scale(
                self.cell_image,
                (
                    self.board_rect.width/self.board.column,
                    self.board_rect.height/self.board.column))
        for col in range(self.board.column):
            for ro in range(self.board.row):
                self.window.WIN.blit(
                    self.cell,
                    (
                        self.board_rect.x + self.cell.get_width()*col,
                        self.board_rect.y + self.cell.get_height()*ro))

    def displaying_pawns(self):
        """checks for placement of pawns and displays them"""
        white = pygame.transform.scale(
            self.white,
            (self.cell.get_width() * 0.9, self.cell.get_height() * 0.9))
        white_x = (
            self.board_rect.x + (self.cell.get_width() - white.get_width())/2)
        white_y = (
            self.board_rect.y + (
                self.cell.get_height() - white.get_height())/2)

        black = pygame.transform.scale(
            self.black,
            (self.cell.get_width() * 0.9, self.cell.get_height() * 0.9))
        black_x = (
            self.board_rect.x + (self.cell.get_width() - black.get_width())/2)
        black_y = (
            self.board_rect.y + (
                self.cell.get_height() - black.get_height())/2)

        for column in range(self.board.column):
            for row in range(self.board.row):
                if self.board.board[row][column] == BLACK:
                    self.window.WIN.blit(
                        black,
                        (
                            black_x + self.cell.get_width()*column,
                            black_y + self.cell.get_height()*row))
                if self.board.board[row][column] == WHITE:
                    self.window.WIN.blit(
                        white,
                        (
                            white_x + self.cell.get_width()*column,
                            white_y + self.cell.get_height()*row))

    def display_points(self):
        """displays points in real time"""
        # updating rectangles size
        white_score_rect = self.white_score_rectangle()
        self.white_score_rect.update(white_score_rect)
        black_score_rect = self.black_score_rectangle()
        self.black_score_rect.update(black_score_rect)
        # displaying black text
        self.window.WIN.blit(
            self.text(BLACK_SCORE),
            (self.black_score_rect.x, self.black_score_rect.y))
        # displaying white text
        self.window.WIN.blit(
            self.text(WHITE_SCORE),
            (self.white_score_rect.x, self.white_score_rect.y))
        # getting real time score
        white_points = str(self.board.count_pieces()[0])
        black_points = str(self.board.count_pieces()[1])
        # displaying points for each player
        self.window.WIN.blit(
            self.text(white_points),
            (self.white_score_rect.right + 10, self.white_score_rect.top))
        self.window.WIN.blit(
            self.text(black_points),
            (self.black_score_rect.right + 10, self.black_score_rect.top))

    def display_turn(self):
        """displays whose turn it is in real time"""
        turn_rect = self.turn_rectangle()
        self.turn_rect.update(turn_rect)
        if self.turn == BLACK:
            self.window.WIN.blit(
                self.text(BLACK_TURN),
                (self.turn_rect.x, self.turn_rect.y))
        elif self.turn == WHITE:
            self.window.WIN.blit(
                self.text(WHITE_TURN),
                (self.turn_rect.x, self.turn_rect.y))

    def display_end(self):
        """displays which player won and allows to restart game"""
        white, black = self.board.count_pieces()[:2]
        font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/6))
        if white > black:
            text = font.render('WHITE WINS', 1, WHITE)
        elif black > white:
            text = font.render("BLACK WINS", 1, WHITE)
        else:
            text = font.render("TIE", 1, WHITE)
        rect = pygame.Rect(
            (self.window.width - text.get_width())/2 - 10,
            (self.window.height - text.get_height())/2 - 10,
            text.get_width() + 20,
            text.get_height() + 15)
        continue_text = self.text('CONTINUE')
        continue_rect = pygame.Rect(
            self.window.width - continue_text.get_width() - 20,
            self.window.height - continue_text.get_height() - 20,
            continue_text.get_width(),
            continue_text.get_height())
        pygame.draw.rect(self.window.WIN, RED, rect)
        self.window.WIN.blit(
            text,
            (rect.x + 10, rect.y + 10))
        self.window.WIN.blit(
            continue_text,
            (continue_rect.x, continue_rect.y))
        mouse_pos = pygame.mouse.get_pos()
        mouse_pres = pygame.mouse.get_pressed()[0]
        if continue_rect.collidepoint(mouse_pos) and mouse_pres:
            self.restart = True

    def game(self):
        """do turns"""
        if not self.board.game_ended():
            if self.turn == BLACK:
                if self.player1.name == 'player':
                    self.player1.make_move(self.mouse_input)
                else:
                    self.player1.make_move()
                if self.empty > self.board.count_pieces()[2] or \
                   self.board.get_valid_moves(BLACK) == []:
                    self.turn = WHITE
                    self.empty -= 1

            if self.turn == WHITE:
                if self.player2.name == 'player':
                    self.player2.make_move(self.mouse_input)
                else:
                    self.player2.make_move()
                if self.empty > self.board.count_pieces()[2] or \
                   self.board.get_valid_moves(WHITE) == []:
                    self.turn = BLACK
                    self.empty -= 1

    def display(self):
        """displays everything onto the screen"""

        self.window.display()

        self.displaying_board()
        self.displaying_pawns()

        self.display_points()
        self.display_turn()
        if self.board.game_ended():
            self.display_end()
