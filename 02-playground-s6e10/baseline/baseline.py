"""Claude's generic LightGBM baseline for a Playground Series episode (badge only).

Target column = the non-id column of sample_submission.csv. Binary targets get probabilities,
otherwise regression. Check the competition's Evaluation tab before trusting this.

Usage: python baseline.py [episode-folder]   (default: the folder this script belongs to)
"""
import sys
from pathlib import Path

import lightgbm as lgb
import pandas as pd

HERE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
DATA, OUT = HERE / "data", HERE / "submissions"

train = pd.read_csv(DATA / "train.csv")
test = pd.read_csv(DATA / "test.csv")
sample = pd.read_csv(DATA / "sample_submission.csv")
id_col, target = sample.columns[0], sample.columns[1]

X = train.drop(columns=[id_col, target])
X_test = test[X.columns].copy()
for col in X.select_dtypes(exclude="number").columns:
    X[col] = X[col].astype("category")
    X_test[col] = pd.Categorical(X_test[col], categories=X[col].cat.categories)

y = train[target]
if y.nunique() == 2:
    classes = sorted(y.unique())
    model = lgb.LGBMClassifier(n_estimators=500, learning_rate=0.05, verbose=-1)
    model.fit(X, (y == classes[1]).astype(int))
    pred = model.predict_proba(X_test)[:, 1]
else:
    model = lgb.LGBMRegressor(n_estimators=500, learning_rate=0.05, verbose=-1)
    model.fit(X, y)
    pred = model.predict(X_test)

OUT.mkdir(exist_ok=True)
pd.DataFrame({id_col: test[id_col], target: pred}).to_csv(OUT / "baseline.csv", index=False)
print("target:", target, "| wrote", OUT / "baseline.csv")
