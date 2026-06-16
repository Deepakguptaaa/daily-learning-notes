from sklearn.linear_model import LinearRegression
import numpy as np

# Realistic dataset: Advertising spend vs Sales
X = np.array([
    [100], [200], [300], [400], [500], [600]
])  # ad spend in $

y = np.array([
    1000, 1900, 2900, 4100, 5000, 6100
])  # sales

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[450]])

print("Predicted Sales:", prediction[0])