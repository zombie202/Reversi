import pygame
import os
from window import Window
from board import Board
from player import Player
from computer import Computer
pygame.font.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK_SCORE = 'BLACK:'
WHITE_SCORE = 'WHITE:'
BLACK_TURN = 'BLACK TURN'
WHITE_TURN = 'WHITE TURN'


class Game(Window, Board):

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

    def text(self, text):
        score_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/12))
        return score_font.render(text, 1, WHITE)

    def text_width(self, text):
        return self.text(text).get_width()

    def text_height(self, text):
        return self.text(text).get_height()

    def board_rectangle(self):
        return pygame.Rect(
            (self.window.width - self.window.height - self.window.height/20)/2,
            self.window.height/40,
            self.window.height - self.window.height/20,
            self.window.height - self.window.height/20)

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

    def get_mouse_input(self, event):
        rect = self.board_rectangle()
        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos_x > rect.right or \
               mouse_pos_x < rect.left or \
               mouse_pos_y > rect.bottom or \
               mouse_pos_y < rect.top:
                print('outside')
                pass
            else:
                column = (mouse_pos_x - self.board_rect.left) // \
                    self.cell.get_width()
                row = (mouse_pos_y - self.board_rect.top) // \
                    self.cell.get_height()
                position = (row, column)
                self.mouse_input = position
                print(self.mouse_input)

    def displaying_board(self):
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
        # display board
        for col in range(self.board.column):
            for ro in range(self.board.row):
                self.window.WIN.blit(
                    self.cell,
                    (
                        self.board_rect.x + self.cell.get_width()*col,
                        self.board_rect.y + self.cell.get_height()*ro))

    def displaying_pawns(self):
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

    def game(self):
        if not self.board.game_ended():
            if self.turn == BLACK:
                if self.player1.name == 'player':
                    self.player1.make_move(self.mouse_input)
                    if self.empty > self.board.count_pieces()[2]:
                        self.turn = WHITE
                        self.empty -= 1
                else:
                    self.player1.make_move()
                    if self.empty > self.board.count_pieces()[2]:
                        self.turn = WHITE
                        self.empty -= 1

            if self.turn == WHITE:
                if self.player2.name == 'player':
                    self.player2.make_move(self.mouse_input)
                    if self.empty > self.board.count_pieces()[2]:
                        self.turn = BLACK
                        self.empty -= 1
                else:
                    self.player2.make_move()
                    if self.empty > self.board.count_pieces()[2]:
                        self.turn = BLACK
                        self.empty -= 1

    def display(self):

        self.window.display()

        self.displaying_board()
        self.displaying_pawns()

        self.display_points()
        self.display_turn()
