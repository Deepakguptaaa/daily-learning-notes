# Decision Trees

## What is a Decision Tree?

A Decision Tree is a supervised machine learning algorithm used for both classification and regression tasks.

It makes decisions by splitting data into smaller groups based on feature values.

## How Does It Work?

A Decision Tree starts with a root node and asks questions about the data.

Example:

Is Age > 18?

├── Yes → Eligible to Vote
└── No → Not Eligible to Vote

The tree keeps splitting until it reaches a final decision.

## Real-World Example

Suppose a bank wants to decide whether to approve a loan.

Questions may be:

- Income > ₹50,000?
- Credit Score > 700?
- Existing Loan = No?

Based on the answers, the model predicts:

- Loan Approved ✅
- Loan Rejected ❌

## Important Concepts

### Entropy

Entropy measures the amount of uncertainty in the data.

Lower entropy means the data is more organized.

### Information Gain

Information Gain helps decide which question should be asked first.

The feature with the highest Information Gain is chosen for the split.

## Advantages

- Easy to understand
- Easy to visualize
- Works with numerical and categorical data
- Requires little data preprocessing

## Limitations

- Can overfit the training data
- Sensitive to small data changes
- Large trees can become complex

## Python Example

```python
from sklearn.tree import DecisionTreeClassifier

X = [[20], [25], [30], [35]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[28]])
print(prediction)
```

## Applications

- Loan approval
- Medical diagnosis
- Fraud detection
- Customer churn prediction

## What I Learned

- Decision Trees are supervised learning algorithms.
- They work by asking questions and splitting data.
- Information Gain helps choose the best split.