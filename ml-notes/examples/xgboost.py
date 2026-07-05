from xgboost import XGBClassifier
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42,
    eval_metric="mlogloss"
)

model.fit(X, y)

print("Training Accuracy:", model.score(X, y))