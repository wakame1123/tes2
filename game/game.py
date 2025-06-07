from .board import Board
from .pieces import shogi_pawn, chess_pawn, king, gold, rook

class Game:
    def __init__(self):
        self.board = Board()
        self.setup_board()

    def setup_board(self):
        # Place shogi pieces on bottom rows
        for x in range(9):
            pawn = shogi_pawn()
            pawn.x, pawn.y = x, 6
            self.board.place_piece(pawn, x, 6)
        self.place_piece(gold('shogi'), 4, 8)
        self.place_piece(king('shogi'), 3, 8)
        # Place chess pieces on top rows
        for x in range(9):
            pawn = chess_pawn()
            pawn.x, pawn.y = x, 1
            self.board.place_piece(pawn, x, 1)
        self.place_piece(rook('chess'), 0, 0)
        self.place_piece(king('chess'), 4, 0)

    def place_piece(self, piece, x, y):
        piece.x = x
        piece.y = y
        self.board.place_piece(piece, x, y)

    def possible_moves(self, x, y):
        piece = self.board.get_piece(x, y)
        if piece:
            return piece.possible_moves(self.board)
        return []

    def move(self, from_x, from_y, to_x, to_y):
        piece = self.board.get_piece(from_x, from_y)
        if piece and (to_x, to_y) in piece.possible_moves(self.board):
            self.board.move_piece(from_x, from_y, to_x, to_y)
            return True
        return False

    def __str__(self):
        return str(self.board)
