"""Titanic helpers to be imported from other notebooks (utility script badge).

In a notebook: Add Input -> Your Work -> this script, then `from titanic_utils import prepare`.
"""
import pandas as pd

FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]


def prepare(df: pd.DataFrame) -> pd.DataFrame:
    x = df[FEATURES].copy()
    x["Sex"] = (x["Sex"] == "female").astype(int)
    x["Embarked"] = x["Embarked"].fillna("S").map({"S": 0, "C": 1, "Q": 2})
    return x.fillna({"Age": 28.0, "Fare": 14.45})


def title_from_name(name: str) -> str:
    title = name.split(",")[1].split(".")[0].strip()
    return title if title in {"Mr", "Mrs", "Miss", "Master"} else "Rare"
