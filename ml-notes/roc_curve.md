# ROC Curve

## What is a ROC Curve?

The ROC (Receiver Operating Characteristic) Curve is a graph used to evaluate the performance of a binary classification model.

It shows how well a model distinguishes between positive and negative classes by plotting the True Positive Rate (TPR) against the False Positive Rate (FPR).

## True Positive Rate (TPR)

True Positive Rate is also called **Recall** or **Sensitivity**.

Formula:

TPR = TP / (TP + FN)

A higher TPR means the model correctly identifies more positive cases.

## False Positive Rate (FPR)

False Positive Rate measures how often the model incorrectly predicts a negative sample as positive.

Formula:

FPR = FP / (FP + TN)

A lower FPR indicates fewer false alarms.

## Area Under the Curve (AUC)

AUC (Area Under the ROC Curve) measures the overall ability of the model to distinguish between classes.

* AUC = 1.0 → Perfect model
* AUC = 0.5 → Random guessing
* Higher AUC indicates better model performance.

## Advantages

* Evaluates classification models at different thresholds.
* Useful for comparing multiple classifiers.
* Less affected by class imbalance than accuracy alone.

## Applications

* Medical diagnosis
* Fraud detection
* Spam email filtering
* Credit risk analysis

## What I Learned

* ROC Curve evaluates binary classification models.
* TPR measures correctly identified positives.
* FPR measures incorrect positive predictions.
* AUC summarizes model performance into a single score.
