from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2

iris = load_iris()

X = iris.data
y = iris.target

selector = SelectKBest(score_func=chi2, k=2)
X_new = selector.fit_transform(X, y)

print("Original Shape:", X.shape)
print("Selected Shape:", X_new.shape)