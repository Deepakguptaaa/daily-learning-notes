# K-Nearest Neighbors (KNN)

## What is KNN?

KNN is a supervised machine learning algorithm used for classification and regression.

It works by finding the **K closest data points** to a new input and making a decision based on them.

## How it works?

1. Choose value of K (example: 3 or 5)
2. Find nearest neighbors using distance (usually Euclidean distance)
3. Take majority vote (classification)
4. Assign result

## Real-World Example

Suppose you want to classify a fruit:

- Apple 🍎
- Orange 🍊

If a new fruit looks more similar to apples around it, KNN will classify it as Apple.

## Python Example

```python
from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [6], [7]]
y = [0, 0, 0, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print(model.predict([[4]]))
```

## Advantages

- Simple and easy to understand
- No training phase (lazy learning)
- Works well with small datasets

## Limitations

- Slow for large datasets
- Sensitive to irrelevant features
- Needs good choice of K

## What I Learned

- KNN uses distance-based learning
- It is a lazy algorithm
- It classifies based on nearest neighbors
```