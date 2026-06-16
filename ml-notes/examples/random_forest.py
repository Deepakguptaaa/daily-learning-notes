import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from utils.path_config import DATA_PATH

df = pd.read_csv(DATA_PATH)

X = df[["income", "age"]]
y = df["loan_approved"]

model = RandomForestClassifier()
model.fit(X, y)

print("Prediction:", model.predict([[70000, 40]])[0])