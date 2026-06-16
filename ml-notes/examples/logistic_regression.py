import pandas as pd
from sklearn.linear_model import LogisticRegression
from utils.path_config import DATA_PATH

df = pd.read_csv(DATA_PATH)

X = df[["income", "age"]]
y = df["loan_approved"]

model = LogisticRegression()
model.fit(X, y)

print("Prediction:", model.predict([[45000, 30]])[0])