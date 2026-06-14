from sklearn.linear_model import LinearRegression
import numpy as np

# House size (sq ft)
X = np.array([[1000], [1500], [2000], [2500], [3000]])

# House price (Lakhs)
y = np.array([30, 45, 60, 75, 90])

model = LinearRegression()
model.fit(X, y)

new_house = np.array([[1800]])

prediction = model.predict(new_house)

print(f"Predicted House Price: ₹{prediction[0]:.2f} Lakhs")