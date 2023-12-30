WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMPTY = 'empty'


class Board:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board = [[EMPTY] * column for elem in range(row)]
        self.board[int(row/2) - 1][int(column/2) - 1] = BLACK
        self.board[int(row/2) - 1][int(column/2)] = WHITE
        self.board[int(row/2)][int(column/2) - 1] = WHITE
        self.board[int(row/2)][int(column/2)] = BLACK
        self.valid_moves = []

    def get_valid_moves(self, color):
        places = []

        for a in range(self.row):
            for b in range(self.column):
                if self.board[a][b] == color:
                    places = places + self.check_directions(a, b, color)

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

    def check_directions(self, row, column, color):
        if color == WHITE:
            other = BLACK
        else:
            other = WHITE

        places = []

        if row not in range(self.row) or column not in range(self.column):
            return places

        for (x, y) in [(x, y) for x in range(-1, 2) for y in range(-1, 2)
                       if (x, y) != (0, 0)]:
            position = self.check_for_empty(row, column, x, y, other)
            if position:
                places.append(position)

        return places
