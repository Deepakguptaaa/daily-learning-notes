from catboost import CatBoostClassifier
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

model = CatBoostClassifier(
    iterations=100,
    learning_rate=0.1,
    depth=6,
    verbose=0,
    random_state=42
)

model.fit(X, y)

print("Training Accuracy:", model.score(X, y))