"""Generate ConnectX self-play logs (original data, CC0) for the dataset badges."""
import sys
from pathlib import Path

import pandas as pd
from kaggle_environments import make

HERE = Path(__file__).resolve().parent
AGENT = str(HERE.parents[1] / "03-simulation-connectx" / "baseline" / "submission.py")
GAMES_PER_PAIRING = int(sys.argv[1]) if len(sys.argv) > 1 else 100

moves, games = [], []
game_id = 0
for opponent in ("random", "negamax"):
    for first in (True, False):
        for _ in range(GAMES_PER_PAIRING // 2):
            players = [AGENT, opponent] if first else [opponent, AGENT]
            names = ["heuristic" if p == AGENT else p for p in players]
            env = make("connectx", debug=False)
            env.run(players)
            for step_no, step in enumerate(env.steps[1:], start=1):
                for mark, s in enumerate(step, start=1):
                    if s.action is not None and env.steps[step_no - 1][mark - 1].status == "ACTIVE":
                        moves.append({"game_id": game_id, "move_no": step_no, "player_mark": mark,
                                      "agent": names[mark - 1], "column": int(s.action)})
            final = env.steps[-1]
            winner = next((i + 1 for i, s in enumerate(final) if s.reward == 1), 0)
            games.append({"game_id": game_id, "agent_1": names[0], "agent_2": names[1],
                          "winner_mark": winner, "n_moves": len(env.steps) - 1})
            game_id += 1

out = HERE / "upload"
pd.DataFrame(games).to_csv(out / "games.csv", index=False)
pd.DataFrame(moves).to_csv(out / "moves.csv", index=False)
print(len(games), "games,", len(moves), "moves")
