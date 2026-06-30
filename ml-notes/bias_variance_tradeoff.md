# Bias-Variance Tradeoff

## What is Bias?

Bias is the error caused by making overly simple assumptions in a machine learning model.

A high-bias model may fail to capture important patterns in the data.

This usually leads to underfitting.

## What is Variance?

Variance measures how much a model changes when trained on different datasets.

A high-variance model fits the training data too closely and may perform poorly on unseen data.

This usually leads to overfitting.

## Underfitting

Underfitting occurs when the model is too simple to learn the underlying patterns.

Characteristics:

* High Bias
* Low Variance
* Poor performance on both training and testing data

## Overfitting

Overfitting occurs when the model memorizes the training data instead of learning general patterns.

Characteristics:

* Low Bias
* High Variance
* Excellent training accuracy
* Poor testing accuracy

## Bias-Variance Tradeoff

A good machine learning model balances bias and variance.

The goal is to reduce both as much as possible while maintaining good performance on unseen data.

## Real-World Example

Imagine predicting house prices.

* A very simple model may ignore important features (high bias).
* A very complex model may memorize every house in the training set (high variance).

A balanced model performs well on both training and new data.

## Applications

* Model selection
* Hyperparameter tuning
* Preventing overfitting
* Improving prediction accuracy

## What I Learned

* High bias causes underfitting.
* High variance causes overfitting.
* A balanced model generalizes better to new data.
* The bias-variance tradeoff is a key concept in machine learning.
