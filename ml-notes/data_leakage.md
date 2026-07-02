# Data Leakage

## What is Data Leakage?

Data Leakage occurs when information that would not be available during real-world prediction is accidentally used during model training.

This causes unrealistically high performance during evaluation.

## Why is Data Leakage a Problem?

* Produces misleading accuracy.
* Models fail on new data.
* Gives false confidence in model performance.

## Common Causes

* Using test data during training.
* Scaling the entire dataset before splitting.
* Including future information in training data.
* Incorrect feature engineering.

## How to Prevent Data Leakage

* Split data before preprocessing.
* Keep training and testing data separate.
* Build preprocessing pipelines.
* Validate models carefully.

## Applications

Preventing data leakage is important in:

* Medical diagnosis
* Fraud detection
* Financial forecasting
* Customer analytics

## What I Learned

* Data leakage leads to unrealistic model performance.
* Proper train/test separation is essential.
* ML pipelines help avoid leakage.
