from lightgbm import LGBMClassifier
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

model = LGBMClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)

model.fit(X, y)

print("Training Accuracy:", model.score(X, y))