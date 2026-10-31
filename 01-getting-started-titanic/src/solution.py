"""YOUR implementation. Fill in each TODO, then ask Claude to review before submitting.

Run:  python src/solution.py
Goal: beat the baseline public score (see ../README.md).
"""
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent.parent
DATA, OUT = HERE / "data", HERE / "submissions"


def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    # TODO 1: read train.csv and test.csv
    raise NotImplementedError


def engineer(df: pd.DataFrame) -> pd.DataFrame:
    # TODO 2: feature engineering
    #   - Title extracted from Name (Mr, Mrs, Miss, Master, rare)
    #   - FamilySize = SibSp + Parch + 1, IsAlone
    #   - fill Age by median per Title, fill Fare / Embarked
    #   - encode categoricals
    raise NotImplementedError


def validate(X, y) -> float:
    # TODO 3: StratifiedKFold CV, return mean accuracy. Try >= 2 models.
    raise NotImplementedError


def main() -> None:
    # TODO 4: load -> engineer -> validate -> fit on full train -> predict test
    # TODO 5: save to OUT / "solution.csv" with columns PassengerId, Survived (int)
    raise NotImplementedError


if __name__ == "__main__":
    main()
