# Cross Validation

## What is Cross Validation?

Cross Validation is a technique used to evaluate the performance of a Machine Learning model on unseen data.

Instead of training and testing the model only once, the dataset is divided into multiple parts and the model is tested multiple times.

This provides a more reliable estimate of model performance.

## Why Train/Test Split is Not Always Enough

A single train/test split may give misleading results because:

* The test set may be too easy or too difficult.
* Results can vary depending on how the data is split.
* The model may appear better or worse than it actually is.

Cross Validation helps reduce this problem by evaluating the model on different subsets of data.

## K-Fold Cross Validation

K-Fold Cross Validation is the most common type of cross validation.

Steps:

1. Split the dataset into K equal parts (folds).
2. Use one fold for testing and the remaining folds for training.
3. Repeat the process K times.
4. Calculate the average performance score.

Example:

For K = 5:

* Fold 1 → Test, Remaining → Train
* Fold 2 → Test, Remaining → Train
* Fold 3 → Test, Remaining → Train
* Fold 4 → Test, Remaining → Train
* Fold 5 → Test, Remaining → Train

Final Score = Average of all 5 results

## Advantages

* More reliable model evaluation
* Better use of available data
* Reduces bias from a single train/test split
* Helps detect overfitting

## Applications

* Model evaluation
* Hyperparameter tuning
* Comparing different algorithms
* Machine Learning competitions
* Real-world predictive systems

## What I Learned

* Cross Validation provides a better estimate of model performance.
* K-Fold Cross Validation is widely used in Machine Learning.
* It reduces the risk of misleading evaluation results.
* It helps select the best model for a problem.
