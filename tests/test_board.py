from board import Board


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMPTY = 'empty'


def test_board():
    board = Board(8, 8)
    assert board.board[3][3] == BLACK
    assert board.board[4][4] == BLACK
    assert board.board[3][4] == WHITE
    assert board.board[4][3] == WHITE


def test_count_start_pieces():
    board = Board(8, 8)
    white, black, empty = board.count_pieces()
    assert white == 2
    assert black == 2
    assert empty == 60


def test_count_pieces():
    board = Board(8, 8)
    board.board[0][0] = BLACK
    board.board[0][1] = WHITE
    board.board[1][1] = BLACK
    white, black, empty = board.count_pieces()
    assert white == 3
    assert black == 4
    assert empty == 57


def test_valid_moves():
    board = Board(8, 8)
    a = board.get_valid_moves(BLACK)
    assert a == [(3, 5), (5, 3), (2, 4), (4, 2)]
    assert board.valid_moves == [(3, 5), (5, 3), (2, 4), (4, 2)]


def test_check_flip_directions():
    board = Board(8, 8)
    a = board.check_flip_direction(4, 2, BLACK)
    assert a == [(0, 1)]


def test_make_move():
    board = Board(8, 8)
    board.make_move((3, 5), BLACK)
    assert board.board[3][5] == BLACK
