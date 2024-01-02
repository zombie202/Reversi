class Player:

    def __init__(self, board, color, label):
        self.board = board
        self.color = color
        self.label = label

    def make_move(self, position):
        self.board.make_move(position, self.color)
