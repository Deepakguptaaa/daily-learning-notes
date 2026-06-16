import pandas as pd
from sklearn.linear_model import LinearRegression
from utils.path_config import DATA_PATH

df = pd.read_csv(DATA_PATH)

X = df[["income"]]
y = df["age"]

model = LinearRegression()
model.fit(X, y)

print("Prediction:", model.predict([[55000]])[0])