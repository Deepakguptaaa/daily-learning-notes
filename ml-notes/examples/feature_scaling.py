from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([
    [1000],
    [2000],
    [3000],
    [4000],
    [5000]
])

scaler = StandardScaler()

scaled = scaler.fit_transform(X)

print(scaled)