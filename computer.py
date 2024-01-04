WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Computer:
    def __init__(self, board, color):
        self.board = board
        self.color = color
        self.name = 'computer'

    def check_for_color(self, row, column, row_add, col_add, color):

        if color == WHITE:
            other_color = BLACK
        else:
            other_color = WHITE

        count = 0
        a = row + row_add
        b = column + col_add
        if a >= 0 and b >= 0 and a < self.board.row and b < self.board.column \
           and self.board.board[a][b] == other_color:
            a += row_add
            b += col_add
            count += 1
            while a >= 0 and b >= 0 and a < self.board.row and \
                    b < self.board.column and \
                    self.board.board[a][b] == other_color:
                a += row_add
                b += col_add
                count += 1
            if a >= 0 and b >= 0 and a < self.board.row and \
               b < self.board.column and self.board.board[a][b] == color:
                return count

    def count_in_directions(self, row, column, color):

        directions = 0

        if row not in range(self.board.row) or \
           column not in range(self.board.column):
            return directions

        for (x, y) in [(x, y) for x in range(-1, 2) for y in range(-1, 2)
                       if (x, y) != (0, 0)]:
            direction = self.check_for_color(row, column, x, y, color)
            if direction:
                directions += direction

        return directions

    def count_in_position(self):
        position = ()
        counter = 0
        for (x, y) in self.board.get_valid_moves(self.color):
            count = self.count_in_directions(x, y, self.color)
            if count > counter:
                counter = count
                position = (x, y)
        return position

    def make_move(self):
        self.board.make_move(self.count_in_position(), self.color)
