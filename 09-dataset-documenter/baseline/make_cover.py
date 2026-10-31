"""Draw the dataset cover: the final board of the longest heuristic-vs-negamax game."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Circle, Rectangle

UPLOAD = Path(__file__).resolve().parent / "upload"
ROWS, COLS = 6, 7
COLORS = {0: "#10243f", 1: "#f4c430", 2: "#e4572e"}

games = pd.read_csv(UPLOAD / "games.csv")
moves = pd.read_csv(UPLOAD / "moves.csv")
vs_negamax = games[(games.agent_1 == "negamax") | (games.agent_2 == "negamax")]
game_id = vs_negamax.loc[vs_negamax.n_moves.idxmax(), "game_id"]

board = [[0] * COLS for _ in range(ROWS)]
for m in moves[moves.game_id == game_id].sort_values("move_no").itertuples():
    row = max(r for r in range(ROWS) if board[r][m.column] == 0)
    board[row][m.column] = m.player_mark

fig = plt.figure(figsize=(5.6, 2.8), dpi=200, facecolor="#0b1a2e")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 560)
ax.set_ylim(0, 280)
ax.axis("off")
cell = 36
left, bottom = 280 - cell * COLS / 2, 140 - cell * ROWS / 2
ax.add_patch(Rectangle((left - 6, bottom - 6), cell * COLS + 12, cell * ROWS + 12, color="#1f5fa8"))
for r in range(ROWS):
    for c in range(COLS):
        center = (left + (c + 0.5) * cell, bottom + (ROWS - r - 0.5) * cell)
        ax.add_patch(Circle(center, cell * 0.41, color=COLORS[board[r][c]]))
fig.savefig(UPLOAD / "dataset-cover-image.png", facecolor=fig.get_facecolor())
print("game", game_id)
