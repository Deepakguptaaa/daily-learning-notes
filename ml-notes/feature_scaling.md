# Feature Scaling

## What is Feature Scaling?

Feature Scaling is a preprocessing technique used to bring all features to a similar scale.

It prevents features with larger values from dominating features with smaller values.

## Why is Feature Scaling Important?

Without feature scaling:

* Distance-based algorithms may give incorrect results.
* Features with large values can dominate model training.
* Training may become slower.

## Standardization

Standardization transforms data so that it has:

* Mean = 0
* Standard Deviation = 1

It is commonly used with:

* Logistic Regression
* SVM
* KNN
* Neural Networks

## Normalization

Normalization scales values between 0 and 1.

It is useful when the data has different ranges or when algorithms require bounded input values.

## Algorithms That Need Feature Scaling

* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Logistic Regression
* K-Means Clustering
* Neural Networks

## Algorithms That Usually Do Not Need Feature Scaling

* Decision Tree
* Random Forest

## Applications

* Customer segmentation
* Image processing
* Medical diagnosis
* Recommendation systems

## What I Learned

* Feature Scaling improves model performance.
* Standardization and Normalization are common scaling techniques.
* Distance-based algorithms benefit significantly from feature scaling.
