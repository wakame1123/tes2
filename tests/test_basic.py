from game.game import Game

def test_setup_board():
    g = Game()
    # there should be 9 shogi pawns at row 6
    count = sum(1 for x in range(9) if g.board.get_piece(x,6))
    assert count == 9


def test_move_pawn():
    g = Game()
    # move shogi pawn at (0,6) forward to (0,5)
    moved = g.move(0,6,0,5)
    assert moved
    assert g.board.get_piece(0,5) is not None
