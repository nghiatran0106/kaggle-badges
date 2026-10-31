"""Play an agent file against built-in agents. Usage: python baseline/evaluate.py <agent.py>"""
import sys

from kaggle_environments import evaluate

path = sys.argv[1] if len(sys.argv) > 1 else "baseline/submission.py"
for opponent in ("random", "negamax"):
    results = evaluate("connectx", [path, opponent], num_episodes=10)
    wins = sum(1 for r in results if r[0] == 1)
    print(f"vs {opponent}: {wins}/10 wins")
