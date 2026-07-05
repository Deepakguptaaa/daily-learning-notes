from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

model.fit(X, y)

print("Training Accuracy:", model.score(X, y))
