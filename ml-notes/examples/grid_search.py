from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = iris.data
y = iris.target

parameters = {
    "n_neighbors": [3, 5, 7, 9]
}

grid = GridSearchCV(
    KNeighborsClassifier(),
    parameters,
    cv=5
)

grid.fit(X, y)

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)