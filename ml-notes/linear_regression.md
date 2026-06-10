# Linear Regression

## What is Linear Regression?

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values.

It finds the relationship between input variables (features) and an output variable (target) by fitting the best straight line through the data.

## Formula

The equation of a straight line is:

y = mx + b

Where:

- y = predicted value
- x = input feature
- m = slope of the line
- b = intercept

## Real-World Example

Suppose we want to predict house prices based on house size.

| House Size (sq ft) | Price (₹ Lakhs) |
|-------------------|----------------|
| 1000 | 30 |
| 1500 | 45 |
| 2000 | 60 |

A Linear Regression model learns the relationship between size and price and can predict the price of a new house.

## Applications

- House price prediction
- Sales forecasting
- Demand prediction
- Stock trend analysis
- Business analytics

## Advantages

- Easy to understand
- Fast to train
- Works well for simple relationships
- Easy to interpret

## Limitations

- Assumes a linear relationship
- Sensitive to outliers
- Cannot capture complex patterns

## Python Example

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])
print(prediction)
```

## What I Learned

- Linear Regression is a supervised learning algorithm.
- It predicts continuous values.
- It uses a straight line to model data.
- It is one of the most fundamental ML algorithms.