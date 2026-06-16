import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from utils.path_config import DATA_PATH

df = pd.read_csv(DATA_PATH)

X = df[["age", "spam_score"]]
y = df["sentiment"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("Prediction:", model.predict([[30, 0.5]])[0])