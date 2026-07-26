from lime.lime_tabular import LimeTabularExplainer
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

explainer = LimeTabularExplainer(
    X,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    mode="classification"
)

print("LIME explainer created successfully.")