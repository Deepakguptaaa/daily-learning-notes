# Confusion Matrix

## What is a Confusion Matrix?

A Confusion Matrix is a table used to evaluate the performance of a classification model.

It compares the actual values with the predicted values and helps measure how well a model is performing.

## True Positive (TP)

A True Positive occurs when the model correctly predicts a positive class.

Example:

* Actual: Spam
* Predicted: Spam

Result: True Positive

## True Negative (TN)

A True Negative occurs when the model correctly predicts a negative class.

Example:

* Actual: Not Spam
* Predicted: Not Spam

Result: True Negative

## False Positive (FP)

A False Positive occurs when the model incorrectly predicts a positive class.

Example:

* Actual: Not Spam
* Predicted: Spam

Result: False Positive

This is also called a Type I Error.

## False Negative (FN)

A False Negative occurs when the model incorrectly predicts a negative class.

Example:

* Actual: Spam
* Predicted: Not Spam

Result: False Negative

This is also called a Type II Error.

## Confusion Matrix Structure

|                 | Predicted Positive | Predicted Negative |
| --------------- | ------------------ | ------------------ |
| Actual Positive | TP                 | FN                 |
| Actual Negative | FP                 | TN                 |

## Accuracy

Accuracy measures the overall correctness of the model.

Formula:

Accuracy = (TP + TN) / (TP + TN + FP + FN)

### Example

If a model correctly predicts 90 out of 100 cases:

Accuracy = 90 / 100 = 90%

## Precision

Precision measures how many predicted positives are actually positive.

Formula:

Precision = TP / (TP + FP)

### Example

If the model predicts 20 emails as spam and 15 are actually spam:

Precision = 15 / 20 = 75%

## Recall

Recall measures how many actual positives are correctly identified.

Formula:

Recall = TP / (TP + FN)

### Example

If there are 20 spam emails and the model finds 15:

Recall = 15 / 20 = 75%

## F1 Score

F1 Score combines Precision and Recall into a single metric.

Formula:

F1 Score = 2 × (Precision × Recall) / (Precision + Recall)

### Why Use F1 Score?

* Useful when classes are imbalanced.
* Balances Precision and Recall.
* Commonly used in classification tasks.

## Applications

* Spam Detection
* Disease Prediction
* Fraud Detection
* Sentiment Analysis
* Customer Churn Prediction

## What I Learned

* A Confusion Matrix evaluates classification models.
* TP, TN, FP, and FN are the foundation of model evaluation.
* Accuracy measures overall correctness.
* Precision measures prediction quality.
* Recall measures detection capability.
* F1 Score balances Precision and Recall.
