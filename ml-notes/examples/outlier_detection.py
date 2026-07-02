import pandas as pd

data = {
    "Salary": [30000, 32000, 31000, 29500, 1000000]
}

df = pd.DataFrame(data)

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]

print("Outliers:")
print(outliers)