import pandas as pd

data = {
    "Age": [21, 25, None, 30, 28],
    "Salary": [30000, None, 50000, 45000, 52000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print("\nAfter Handling Missing Values:")
print(df)