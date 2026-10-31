"""YOUR ConnectX agent. Kaggle imports this file and calls agent(observation, configuration).

observation.board : flat list, rows*cols, 0 empty / 1 / 2, row 0 is the TOP
observation.mark  : your piece (1 or 2)
configuration     : .rows (6), .columns (7), .inarow (4), .timeout
Return            : int column index with board[col] == 0

Test:   python baseline/evaluate.py src/submission.py
Rule:   the file must be self-contained (no imports outside the stdlib / numpy).
"""


def agent(observation, configuration):
    # TODO 1: list valid moves
    # TODO 2: helper that simulates dropping a piece
    # TODO 3: helper that scores a board (count open 2s/3s for you vs opponent)
    # TODO 4: one-step lookahead using the score, then upgrade to minimax/negamax with depth N
    # TODO 5: stay under configuration.timeout (default 2s per move)
    raise NotImplementedError
