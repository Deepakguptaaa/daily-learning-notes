import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "decision_tree_model.pkl")

loaded_model = joblib.load("decision_tree_model.pkl")

print("Training Accuracy:", loaded_model.score(X, y))