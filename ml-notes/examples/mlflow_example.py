import mlflow
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

with mlflow.start_run():

    model = DecisionTreeClassifier(max_depth=3)

    model.fit(X, y)

    accuracy = model.score(X, y)

    mlflow.log_param("max_depth", 3)
    mlflow.log_metric("accuracy", accuracy)

    print("Accuracy:", accuracy)