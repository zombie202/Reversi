WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMPTY = 'empty'


class Board:
    """
    class for handling event on the board takes number of rows
    and number of columns as parameters
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board = [[EMPTY] * column for elem in range(row)]
        self.board[int(row/2) - 1][int(column/2) - 1] = BLACK
        self.board[int(row/2) - 1][int(column/2)] = WHITE
        self.board[int(row/2)][int(column/2) - 1] = WHITE
        self.board[int(row/2)][int(column/2)] = BLACK
        self.valid_moves = []

    def make_move(self, position, color):
        self.get_valid_moves(color)
        if position in self.valid_moves:
            self.board[position[0]][position[1]] = color
            self.flip(position[0], position[1], color)

    """get possible moves player can make ↓"""
    def get_valid_moves(self, color):
        places = []

        for a in range(self.row):
            for b in range(self.column):
                if self.board[a][b] == color:
                    places = places + self.check_move_direction(a, b, color)

        self.valid_moves = places
        return places

    def check_for_empty(self, row, column, row_add, col_add, other_color):
        a = row + row_add
        b = column + col_add
        if a >= 0 and b >= 0 and a < self.row and b < self.column and \
           self.board[a][b] == other_color:
            a += row_add
            b += col_add
            while a >= 0 and b >= 0 and a < self.row and b < self.column and \
                    self.board[a][b] == other_color:
                a += row_add
                b += col_add
            if a >= 0 and b >= 0 and a < self.row and b < self.column and \
               self.board[a][b] == EMPTY:
                return (a, b)

    def check_move_direction(self, row, column, color):
        other = set_other_color(color)

        places = []

        if row not in range(self.row) or column not in range(self.column):
            return places

        for (x, y) in [(x, y) for x in range(-1, 2) for y in range(-1, 2)
                       if (x, y) != (0, 0)]:
            position = self.check_for_empty(row, column, x, y, other)
            if position:
                places.append(position)

        return places
    "↑"

    """flips pawns ↓"""
    def flip(self, row, column, color):
        other_color = set_other_color(color)

        for (x, y) in self.check_flip_direction(row, column, color):
            a = row + x
            b = column + y
            while a >= 0 and b >= 0 and a < self.row and b < self.column:
                if self.board[a][b] == color:
                    break
                if self.board[a][b] == other_color:
                    self.board[a][b] = color
                a += x
                b += y

    def check_for_color(self, row, column, row_add, col_add, color):

        other_color = set_other_color(color)

        a = row + row_add
        b = column + col_add
        if a >= 0 and b >= 0 and a < self.row and b < self.column and \
           self.board[a][b] == other_color:
            a += row_add
            b += col_add
            while a >= 0 and b >= 0 and a < self.row and b < self.column and \
                    self.board[a][b] == other_color:
                a += row_add
                b += col_add
            if a >= 0 and b >= 0 and a < self.row and b < self.column and \
               self.board[a][b] == color:
                return (row_add, col_add)

    def check_flip_direction(self, row, column, color):

        directions = []

        if row not in range(self.row) or column not in range(self.column):
            return directions

        for (x, y) in [(x, y) for x in range(-1, 2) for y in range(-1, 2)
                       if (x, y) != (0, 0)]:
            direction = self.check_for_color(row, column, x, y, color)
            if direction:
                directions.append(direction)

        return directions
    "↑"

    def count_pieces(self):
        """return number of white, black and empty places on the board"""
        white = 0
        black = 0
        empty = 0
        for a in range(self.row):
            for b in range(self.column):
                if self.board[a][b] == WHITE:
                    white += 1
                elif self.board[a][b] == BLACK:
                    black += 1
                else:
                    empty += 1
        return white, black, empty

    def game_ended(self):
        """checks if game has finished"""
        white, black, empty = self.count_pieces()

        if white == 0 or black == 0 or empty == 0:
            return True
        elif self.get_valid_moves(BLACK) == [] and \
                self.get_valid_moves(WHITE) == []:
            return True
        else:
            return False


def set_other_color(color):
    if color == WHITE:
        other_color = BLACK
    else:
        other_color = WHITE
    return other_color
