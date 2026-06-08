# Logistic Regression

## What is Logistic Regression?

Logistic Regression is a supervised machine learning algorithm used for classification problems.

Unlike Linear Regression, it predicts categories rather than continuous values.

## Real-World Example

Suppose we want to predict whether a student will pass an exam.

Input:
- Hours studied = 8

Output:
- Probability of passing = 0.92

Since 0.92 > 0.5, the model predicts:

Pass ✅

If the probability were 0.30, the model would predict:

Fail ❌

## Sigmoid Function

The sigmoid function converts values into probabilities between 0 and 1.

Probability = 1 / (1 + e^-z)

## Applications

- Email spam detection
- Disease prediction
- Fraud detection
- Customer churn prediction

## Python Example

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

model.fit(X, y)

prediction = model.predict([[4]])
print(prediction)
```

## Advantages

- Easy to understand
- Fast to train
- Works well for binary classification

## Limitations

- May not perform well on complex datasets
- Assumes a simple relationship between features and outcome

## Difference Between Linear and Logistic Regression

| Linear Regression | Logistic Regression |
|------------------|---------------------|
| Predicts numbers | Predicts categories |
| Used for regression | Used for classification |

## What I Learned

- Logistic Regression is used for classification.
- It predicts probabilities.
- It uses the sigmoid function.