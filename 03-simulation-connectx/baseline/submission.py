"""Claude's minimal ConnectX agent: win if possible, else block, else prefer center.
Kaggle calls `agent(observation, configuration)` and expects a column index."""


def agent(observation, configuration):
    cols, rows, inarow = configuration.columns, configuration.rows, configuration.inarow
    board = observation.board
    me = observation.mark
    opp = 3 - me

    def valid(c):
        return board[c] == 0

    def drop(b, c, mark):
        b = list(b)
        for r in range(rows - 1, -1, -1):
            if b[r * cols + c] == 0:
                b[r * cols + c] = mark
                return b
        return b

    def wins(b, mark):
        for r in range(rows):
            for c in range(cols):
                for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                    cells = [(r + i * dr, c + i * dc) for i in range(inarow)]
                    if all(0 <= rr < rows and 0 <= cc < cols and b[rr * cols + cc] == mark for rr, cc in cells):
                        return True
        return False

    moves = [c for c in range(cols) if valid(c)]
    for mark in (me, opp):
        for c in moves:
            if wins(drop(board, c, mark), mark):
                return c
    center = cols // 2
    return min(moves, key=lambda c: abs(c - center))
