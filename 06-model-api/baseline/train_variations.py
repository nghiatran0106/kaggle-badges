"""Train two RandomForest sizes on Titanic and save one folder per model variation."""
import pickle
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1] / "01-getting-started-titanic" / "data"

FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]


def prepare(df):
    x = df[FEATURES].copy()
    x["Sex"] = (x["Sex"] == "female").astype(int)
    x["Embarked"] = x["Embarked"].fillna("S").map({"S": 0, "C": 1, "Q": 2})
    return x.fillna({"Age": 28.0, "Fare": 14.45})


train = pd.read_csv(DATA / "train.csv")
X, y = prepare(train), train["Survived"]
for name, n in (("rf-small", 50), ("rf-large", 500)):
    model = RandomForestClassifier(n_estimators=n, max_depth=6, random_state=42).fit(X, y)
    with open(HERE / "variations" / name / "model.pkl", "wb") as f:
        pickle.dump(model, f)
    print(name, "train acc", round(model.score(X, y), 4))
