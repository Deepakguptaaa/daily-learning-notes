# Outlier Detection

## What are Outliers?

Outliers are data points that differ significantly from the rest of the dataset.

They may occur due to measurement errors, data entry mistakes, or genuine rare events.

## Why Detect Outliers?

* Improve model accuracy
* Reduce the effect of noisy data
* Prevent biased predictions
* Improve data quality

## Methods for Detecting Outliers

### 1. Z-Score Method

The Z-score measures how many standard deviations a data point is from the mean.

A value greater than 3 or less than -3 is often considered an outlier.

### 2. Interquartile Range (IQR)

The IQR method identifies outliers using:

* Q1 (25th percentile)
* Q3 (75th percentile)
* IQR = Q3 − Q1

Any value below:

Q1 − 1.5 × IQR

or above:

Q3 + 1.5 × IQR

is considered an outlier.

## Applications

* Fraud detection
* Healthcare analytics
* Financial transactions
* Sensor data analysis

## What I Learned

* Outliers can reduce model performance.
* Z-score and IQR are common detection methods.
* Handling outliers improves data quality.
