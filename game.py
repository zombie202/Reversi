import pygame
import os
from window import Window
from board import Board


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Game(Window, Board):

    def __init__(self, row, column, mode):
        self.window = Window()
        self.board = Board(row, column)

        self.mode = mode

        self.cell_image = pygame.image.load(
            os.path.join('assets', 'cell.png'))
        self.white = pygame.image.load(
            os.path.join('assets', 'bialy_pionek.png'))
        self.black = pygame.image.load(
            os.path.join('assets', 'czarny_pionek.png'))

        self.baord_rect = self.board_rectangle()

    def board_rectangle(self):
        return pygame.Rect(
            (self.window.width - self.window.height - self.window.height/20)/2,
            self.window.height/40,
            self.window.height - self.window.height/20,
            self.window.height - self.window.height/20)

    def get_mouse_input(self, event):
        rect = self.board_rectangle()
        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos_x > rect.right or \
               mouse_pos_x < rect.left or \
               mouse_pos_y > rect.bottom or \
               mouse_pos_y < rect.top:
                pass
            else:
                pass

    def display(self):

        self.window.display()

        board_rect = self.board_rectangle()
        self.baord_rect.update(board_rect)
        if self.board.row > self.board.column:
            self.cell = pygame.transform.scale(
                self.cell_image,
                (
                    self.baord_rect.width/self.board.row,
                    self.baord_rect.height/self.board.row))
        else:
            self.cell = pygame.transform.scale(
                self.cell_image,
                (
                    self.baord_rect.width/self.board.column,
                    self.baord_rect.height/self.board.column))
        # display board
        for col in range(self.board.column):
            for ro in range(self.board.row):
                self.window.WIN.blit(
                    self.cell,
                    (
                        self.baord_rect.x + self.cell.get_width()*col,
                        self.baord_rect.y + self.cell.get_height()*ro))

        # display pawns
        white = pygame.transform.scale(
            self.white,
            (self.cell.get_width() * 0.9, self.cell.get_height() * 0.9))
        wh_x = self.baord_rect.x + (self.cell.get_width() - white.get_width())/2
        wh_y = self.baord_rect.y + (self.cell.get_height() - white.get_height())/2

        black = pygame.transform.scale(
            self.black,
            (self.cell.get_width() * 0.9, self.cell.get_height() * 0.9))
        bl_x = self.baord_rect.x + (self.cell.get_width() - black.get_width())/2
        bl_y = self.baord_rect.y + (self.cell.get_height() - black.get_height())/2

        for column in range(self.board.column):
            for row in range(self.board.row):
                if self.board.board[row][column] == BLACK:
                    self.window.WIN.blit(
                        black,
                        (
                            bl_x + self.cell.get_width()*column,
                            bl_y + self.cell.get_height()*row))
                if self.board.board[row][column] == WHITE:
                    self.window.WIN.blit(
                        white,
                        (
                            wh_x + self.cell.get_width()*column,
                            wh_y + self.cell.get_height()*row))
