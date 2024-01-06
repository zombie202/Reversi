import pygame
from window import Window
import os
pygame.font.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (210, 237, 255)
LIGHT_RED = (255, 100, 100)
LIGHT_GREY = (170, 170, 170)
SELECT = 'Please select board size'
BACK = 'BACK'
CONTINUE = 'CONTINUE'


class BoardSize(Window):
    """class displaying window allowing player to enter board size"""

    def __init__(self):

        self.window = Window()

        self.back_width = self.window.width/22
        self.back_height = self.window.height/13

        self.cell = pygame.image.load(os.path.join('assets', 'cell.png'))
        self.back_image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'back.png')),
            (self.back_width, self.back_height))

        self.back_button = self.back_rect()
        self.continue_button = self.continue_rect()
        self.board_show = self.board_rect()

        self.input_rect_column = self.input_column_rect()
        self.input_column = InputBox(self.input_rect_column, '8 - 30')
        self.input_rect_row = self.input_row_rect()
        self.input_row = InputBox(self.input_rect_row, '8 - 30')
        self.input_box = [self.input_column, self.input_row]

        self.next = False

    def back_text(self):
        back_font = pygame.font.SysFont(
            'comicsans',
            int(self.back_height * 1.5))
        return back_font.render(BACK, 1, WHITE)

    def continue_text(self):
        continue_font = pygame.font.SysFont(
            'comicsans',
            int(self.back_height * 1.5))
        return continue_font.render(CONTINUE, 1, WHITE)

    def select_text(self):
        """render select text"""
        select_font = pygame.font.SysFont(
            'comicsans',
            int(self.window.height/7))
        return select_font.render(SELECT, 1, WHITE)

    """creates rectangle, needed because of different window size ↓"""
    def back_rect(self):
        width = self.window.width
        height = self.window.height
        return pygame.Rect(
            width - width/60 - self.back_text().get_width() - self.back_width,
            height - width/60 - self.back_height,
            self.back_width + self.back_text().get_width(),
            self.back_height)

    def continue_rect(self):
        return pygame.Rect(
            self.back_button.right - self.continue_text().get_width(),
            self.back_button.top - self.continue_text().get_height(),
            self.continue_text().get_width(),
            self.continue_text().get_height())

    def board_rect(self):
        width = self.window.width
        height = self.window.height
        return pygame.Rect(
            (self.window.width - width/3)/2,
            15 * height/130 + self.select_text().get_height() + height/10,
            width/3,
            width/3)

    def input_column_rect(self):
        width = self.window.width
        height = self.window.height
        return pygame.Rect(
            (width - width/15)/2,
            height/13 + self.select_text().get_height() + height/20,
            width/10,
            height/15)

    def input_row_rect(self):
        width = self.window.width
        height = self.window.height
        return pygame.Rect(
            width/1.8 - self.board_show.width,
            self.board_show.top + self.board_show.width/2,
            width/10,
            height/15)
    "↑"

    def middle(self, text):
        """centers the text"""
        return ((self.window.width - text.get_width())/2)

    def input_box_not_wrong(self):
        """checks if input boxes have correct value inside"""
        check_list = []
        for box in self.input_box:
            check_list.append(
                'ok' if box.color != box.color_wrong and box.text != ''
                else 'not ok')
        return (False if 'not ok' in check_list else True)

    def input_box_not_active(self):
        """checks if input boxes is not active"""
        check_list = []
        for box in self.input_box:
            check_list.append(
                'ok' if box.active is False else 'not ok')
        return (False if 'not ok' in check_list else True)

    def get_column_number(self):
        """get column number"""
        if self.input_box_not_wrong() and self.input_box_not_active():
            return int(self.input_column.text)

    def get_row_number(self):
        """get row number"""
        if self.input_box_not_wrong() and self.input_box_not_active():
            return int(self.input_row.text)

    def display_board_preview(self):
        """displays preview of the board on which player will play"""
        # updating rectangle size
        board_show = self.board_rect()
        self.board_show.update(board_show)
        # checks if input box has correct value inside and is not empty
        if self.input_box_not_wrong() and self.input_box_not_active():
            row = int(self.input_row.text)
            column = int(self.input_column.text)
            # scales cell into right square
            if row > column:
                cell = pygame.transform.scale(
                    self.cell,
                    (
                        self.board_show.width/row,
                        self.board_show.height/row))
            else:
                cell = pygame.transform.scale(
                    self.cell,
                    (
                        self.board_show.width/column,
                        self.board_show.height/column))
            # display preview of the board
            for col in range(column):
                for ro in range(row):
                    self.window.WIN.blit(
                        cell,
                        (
                            self.board_show.x + cell.get_width()*col,
                            self.board_show.y + cell.get_height()*ro))

    def display(self):

        self.window.display()

        # displaying select text
        self.window.WIN.blit(
            self.select_text(),
            (self.middle(self.select_text()), self.window.height/13))

        # updating rectangle size
        back_button = self.back_rect()
        self.back_button.update(back_button)
        # displaying back image
        self.window.WIN.blit(
            self.back_image,
            (self.back_button.x, self.back_button.y))

        # displaying back text
        self.window.WIN.blit(
            self.back_text(),
            (self.back_button.x + self.back_width, self.back_button.y))

        # updating rectangle size
        input_rect_column = self.input_column_rect()
        self.input_rect_column.update(input_rect_column)

        # updating rectangle size
        input_rect_row = self.input_row_rect()
        self.input_rect_row.update(input_rect_row)

        # displaying input boxes
        for box in self.input_box:
            box.display(self.window.WIN)

        self.display_board_preview()

        # displaying continue button
        if self.input_box_not_wrong() and self.input_box_not_active():
            self.next = True
            continue_button = self.continue_rect()
            self.continue_button.update(continue_button)
            self.window.WIN.blit(
                self.continue_text(),
                (self.continue_button.x, self.continue_button.y))


class InputBox:
    """class for handling input boxes"""
    def __init__(self, rect, background_text='', font='comicsans'):
        self.rect = rect
        self.font = font
        self.color_active = LIGHT_BLUE
        self.color_not_active = WHITE
        self.color_wrong = LIGHT_RED
        self.color = self.color_not_active
        self.background_text = background_text
        self.text = ''
        self.active = False

    def handle_events(self, event, parameter_min=None, parameter_max=None):
        """
        checks if player clicked the box,
        checks if given value is in given parameter
        """
        text_font = pygame.font.SysFont(self.font, self.rect.height)
        mouse_pos = pygame.mouse.get_pos()
        # if player clicks the box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_pos):
                # toogle the active state
                self.active = not self.active
                if self.active:
                    self.text = ''
        # if not
            else:
                self.active = False

        # checks if input is in given parameters
        if self.text.isnumeric():
            if int(self.text) < parameter_min:
                color_not_active = self.color_wrong
            elif int(self.text) > parameter_max:
                color_not_active = self.color_wrong
            else:
                color_not_active = self.color_not_active
        elif self.text == '':
            color_not_active = self.color_not_active
        else:
            color_not_active = self.color_wrong

        # switches beetwen colors of the box
        if self.active:
            self.color = self.color_active
        else:
            self.color = color_not_active

        # get input from player
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = not self.active
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_text = text_font.render(self.text, 1, BLACK)

    def display(self, screen):
        """display input box onto given screen"""
        pygame.draw.rect(screen, self.color, self.rect)
        text_font = pygame.font.SysFont(self.font, self.rect.height)

        background_text = text_font.render(
            self.background_text,
            1,
            LIGHT_GREY)

        if self.text == '':
            # display background text
            screen.blit(
                background_text,
                (
                    self.rect.center[0] - background_text.get_width()/2,
                    self.rect.center[1] - background_text.get_height()/2))
        else:
            # diplay input text
            screen.blit(
                self.text_text,
                (
                    self.rect.center[0] - self.text_text.get_width()/2,
                    self.rect.center[1] - self.text_text.get_height()/2))
