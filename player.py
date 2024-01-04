class Player:

    def __init__(self, board, color):
        self.board = board
        self.color = color
        self.name = 'player'

    def make_move(self, position):
        self.board.make_move(position, self.color)
