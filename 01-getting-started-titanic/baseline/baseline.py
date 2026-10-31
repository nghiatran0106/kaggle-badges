"""Claude's minimal baseline: only to earn the badge. Do not copy, rewrite it yourself in src/."""
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

HERE = Path(__file__).resolve().parent.parent
DATA, OUT = HERE / "data", HERE / "submissions"

FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]


def prepare(df: pd.DataFrame) -> pd.DataFrame:
    x = df[FEATURES].copy()
    x["Sex"] = (x["Sex"] == "female").astype(int)
    x["Embarked"] = x["Embarked"].fillna("S").map({"S": 0, "C": 1, "Q": 2})
    x["Age"] = x["Age"].fillna(28.0)
    x["Fare"] = x["Fare"].fillna(14.45)
    return x


train = pd.read_csv(DATA / "train.csv")
test = pd.read_csv(DATA / "test.csv")
X, y = prepare(train), train["Survived"]

model = RandomForestClassifier(n_estimators=300, max_depth=6, random_state=42)
print(f"CV accuracy: {cross_val_score(model, X, y, cv=5).mean():.4f}")
model.fit(X, y)

OUT.mkdir(exist_ok=True)
pd.DataFrame({"PassengerId": test["PassengerId"], "Survived": model.predict(prepare(test))}).to_csv(
    OUT / "baseline.csv", index=False
)
print("wrote", OUT / "baseline.csv")
