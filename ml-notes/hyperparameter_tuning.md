# Hyperparameter Tuning

## What is Hyperparameter Tuning?

Hyperparameter Tuning is the process of finding the best combination of hyperparameters to improve a machine learning model's performance.

Unlike model parameters, hyperparameters are set before training begins.

## Parameters vs Hyperparameters

### Parameters

* Learned automatically during training.
* Example: Weights in Linear Regression.

### Hyperparameters

* Set manually before training.
* Example:

  * Number of neighbors (K) in KNN
  * Maximum depth in Decision Trees
  * Learning rate

## Why is Hyperparameter Tuning Important?

* Improves model accuracy.
* Reduces overfitting.
* Helps achieve better generalization.
* Finds the optimal model configuration.

## Grid Search

Grid Search tries every possible combination of hyperparameter values.

Example:

```
n_neighbors = [3,5,7]
weights = ['uniform','distance']
```

Every combination is tested, and the best one is selected.

## Random Search

Random Search selects random combinations of hyperparameters instead of trying every combination.

Advantages:

* Faster than Grid Search.
* Works well with large search spaces.

## Applications

* Classification models
* Regression models
* Deep Learning
* Recommendation Systems

## What I Learned

* Hyperparameters control model behavior.
* Grid Search systematically tests combinations.
* Random Search is faster for larger problems.
* Proper tuning can significantly improve model performance.
