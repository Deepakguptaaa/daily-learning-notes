# Random Forest

## What is Random Forest?

Random Forest is a supervised machine learning algorithm used for classification and regression.

It is an ensemble learning method that combines multiple Decision Trees to make better predictions.

## Why Random Forest?

A single Decision Tree can overfit the training data.

Random Forest reduces overfitting by combining the predictions of many trees.

## How Does It Work?

1. Create multiple Decision Trees using random subsets of data.
2. Each tree makes a prediction.
3. The forest combines all predictions.

### Classification

The majority vote wins.

Example:

Tree 1 → Spam

Tree 2 → Spam

Tree 3 → Not Spam

Final Prediction → Spam

### Regression

The average of all predictions is used.

## Real-World Example

Suppose a bank wants to decide whether to approve a loan.

Instead of relying on one Decision Tree, Random Forest uses hundreds of trees.

The final decision is based on the majority opinion of all trees.

## Advantages

- High accuracy
- Reduces overfitting
- Works well on large datasets
- Handles missing values better

## Limitations

- Slower than a single Decision Tree
- Harder to interpret
- Requires more memory

## Python Example

```python
from sklearn.ensemble import RandomForestClassifier

X = [[20], [25], [30], [35]]
y = [0, 0, 1, 1]

model = RandomForestClassifier()
model.fit(X, y)

prediction = model.predict([[28]])
print(prediction)
```

## Applications

- Fraud detection
- Loan approval
- Medical diagnosis
- Customer churn prediction
- Recommendation systems

## What I Learned

- Random Forest is a collection of Decision Trees.
- It improves accuracy using ensemble learning.
- It reduces overfitting compared to a single tree.