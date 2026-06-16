import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from utils.path_config import DATA_PATH

df = pd.read_csv(DATA_PATH)

X = df[["income", "age"]]
y = df["loan_approved"]

model = DecisionTreeClassifier()
model.fit(X, y)

print("Prediction:", model.predict([[60000, 35]])[0])