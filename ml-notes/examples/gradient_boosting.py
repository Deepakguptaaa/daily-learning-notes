from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)

model.fit(X, y)

print("Training Accuracy:", model.score(X, y))