WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Board:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board = [[0] * column for elem in range(row)]
        self.board[int(row/2) - 1][int(column/2) - 1] = BLACK
        self.board[int(row/2) - 1][int(column/2)] = WHITE
        self.board[int(row/2)][int(column/2) - 1] = WHITE
        self.board[int(row/2)][int(column/2)] = BLACK
        self.valid_moves = []
