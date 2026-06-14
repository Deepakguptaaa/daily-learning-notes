# Support Vector Machine (SVM)

## What is SVM?

Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks.

It works by finding the best boundary (called a hyperplane) that separates different classes of data.

## How SVM Works

SVM tries to find a line or boundary that separates data points into different classes.

The goal is to maximize the distance between the boundary and the nearest data points.

A larger margin usually leads to better generalization on unseen data.

## Hyperplane

A hyperplane is the decision boundary used by SVM to separate classes.

For example:

- Class A → Apples 🍎
- Class B → Oranges 🍊

SVM finds the best line that separates apples from oranges.

## Support Vectors

Support Vectors are the data points closest to the hyperplane.

These points are important because they influence the position of the boundary.

Without support vectors, SVM cannot determine the optimal margin.

## Real-World Example

Suppose an email service wants to classify emails as:

- Spam
- Not Spam

SVM analyzes features such as keywords, sender information, and message content.

Based on these features, it predicts whether an email is spam.

## Python Example

```python
from sklearn.svm import SVC

X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

model = SVC()
model.fit(X, y)

prediction = model.predict([[4]])
print(prediction)
```

## Advantages

- Works well on high-dimensional data
- Effective for classification problems
- Can handle complex decision boundaries
- Good performance on small and medium datasets

## Limitations

- Slower on large datasets
- Choosing the correct kernel can be difficult
- Requires careful parameter tuning

## Applications

- Email spam detection
- Image classification
- Face recognition
- Medical diagnosis
- Text classification

## What I Learned

- SVM is a supervised learning algorithm.
- It uses a hyperplane to separate classes.
- Support vectors determine the optimal boundary.
- SVM is widely used for classification tasks.