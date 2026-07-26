import shap
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

print("SHAP values calculated successfully.")