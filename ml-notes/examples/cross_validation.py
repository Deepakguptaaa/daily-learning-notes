from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()

model = DecisionTreeClassifier()

scores = cross_val_score(
    model,
    iris.data,
    iris.target,
    cv=5
)

print("Scores:", scores)
print("Average Score:", scores.mean())