import pygame
import os
from window import Window
from board import Board
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
        self.cell = ()

    def score_text(self, text):
        score_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/12))
        return score_font.render(text, 1, WHITE)

    def score_width(self, text):
        return self.score_text(text).get_width()

    def score_height(self, text):
        return self.score_text(text).get_height()

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
            self.score_width(BLACK_SCORE),
            self.score_height(BLACK_SCORE))

    def white_score_rectangle(self):
        return pygame.Rect(
            self.black_score_rect.left,
            self.black_score_rect.bottom + 10,
            self.score_width(WHITE_SCORE),
            self.score_height(WHITE_SCORE))

    def get_mouse_input(self, event):
        rect = self.board_rectangle()
        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos_x > rect.right or \
               mouse_pos_x < rect.left or \
               mouse_pos_y > rect.bottom or \
               mouse_pos_y < rect.top:
                print('outside')
            else:
                column = (mouse_pos_x - self.board_rect.left) // \
                    self.cell.get_width()
                row = (mouse_pos_y - self.board_rect.top) // \
                    self.cell.get_height()
                position = (row, column)
                print(position)

    def display(self):

        self.window.display()

        # updating rectangles size
        white_score_rect = self.white_score_rectangle()
        self.white_score_rect.update(white_score_rect)
        black_score_rect = self.black_score_rectangle()
        self.black_score_rect.update(black_score_rect)
        # displaying black text
        self.window.WIN.blit(
            self.score_text(BLACK_SCORE),
            (self.black_score_rect.x, self.black_score_rect.y))
        # displaying white text
        self.window.WIN.blit(
            self.score_text(WHITE_SCORE),
            (self.white_score_rect.x, self.white_score_rect.y))
        # getting real time score
        white_points = str(self.board.count_pieces()[0])
        black_points = str(self.board.count_pieces()[1])
        # displaying points for each player
        self.window.WIN.blit(
            self.score_text(white_points),
            (self.white_score_rect.right + 10, self.white_score_rect.top))
        self.window.WIN.blit(
            self.score_text(black_points),
            (self.black_score_rect.right + 10, self.black_score_rect.top))

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

        # display pawns
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
