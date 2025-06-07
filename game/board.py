class Board:
    SIZE = 9

    def __init__(self):
        self.grid = [[None for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def place_piece(self, piece, x, y):
        if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
            self.grid[y][x] = piece

    def move_piece(self, from_x, from_y, to_x, to_y):
        piece = self.grid[from_y][from_x]
        self.grid[from_y][from_x] = None
        self.grid[to_y][to_x] = piece
        if piece:
            piece.x = to_x
            piece.y = to_y
        return piece

    def get_piece(self, x, y):
        return self.grid[y][x]

    def in_bounds(self, x, y):
        return 0 <= x < self.SIZE and 0 <= y < self.SIZE

    def __str__(self):
        lines = []
        for row in self.grid:
            line = []
            for piece in row:
                if piece is None:
                    line.append('. ')
                else:
                    line.append(piece.symbol + ' ')
            lines.append(''.join(line))
        return '\n'.join(lines)
