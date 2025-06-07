class Piece:
    def __init__(self, name, owner, symbol, moves):
        self.name = name
        self.owner = owner  # 'shogi' or 'chess'
        self.symbol = symbol
        self.moves = moves  # list of (dx, dy) tuples
        self.x = 0
        self.y = 0

    def possible_moves(self, board):
        result = []
        for dx, dy in self.moves:
            nx = self.x + dx
            ny = self.y + dy
            if board.in_bounds(nx, ny):
                occupant = board.get_piece(nx, ny)
                if occupant is None or occupant.owner != self.owner:
                    result.append((nx, ny))
        return result

# Basic move sets (simplified)
KING_MOVES = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
GOLD_MOVES = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1)]
PAWN_MOVES_SHOGI = [(0,-1)]
PAWN_MOVES_CHESS = [(0,1)]
ROOK_MOVES = [(1,0),(-1,0),(0,1),(0,-1)]

# Factory functions

def shogi_pawn(owner='shogi'):
    return Piece('shogi_pawn', owner, 'P', PAWN_MOVES_SHOGI)

def chess_pawn(owner='chess'):
    return Piece('chess_pawn', owner, 'p', PAWN_MOVES_CHESS)

def king(owner):
    return Piece('king', owner, 'K' if owner=='shogi' else 'k', KING_MOVES)

def gold(owner='shogi'):
    return Piece('gold', owner, 'G', GOLD_MOVES)

def rook(owner='chess'):
    return Piece('rook', owner, 'r', ROOK_MOVES)
