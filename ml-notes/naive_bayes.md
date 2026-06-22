# Naive Bayes

## What is Naive Bayes?

Naive Bayes is a supervised machine learning algorithm mainly used for classification tasks.

It is based on Bayes' Theorem and assumes that features are independent of each other.

## Bayes Theorem

P(A|B) = (P(B|A) × P(A)) / P(B)

## How It Works

1. Calculate probabilities from training data.
2. Apply Bayes Theorem.
3. Predict the class with the highest probability.

## Real-World Example

Email Spam Detection:

Features:
- Contains "free"
- Contains "offer"
- Contains links

Prediction:
- Spam
- Not Spam

## Advantages

- Fast and efficient
- Works well with text data
- Easy to implement
- Requires less training data

## Limitations

- Assumes feature independence
- Can be less accurate when features are highly related

## Applications

- Spam filtering
- Sentiment analysis
- News classification
- Document categorization

## What I Learned

- Naive Bayes is based on probability.
- It uses Bayes Theorem for prediction.
- It is widely used in text classification tasks.