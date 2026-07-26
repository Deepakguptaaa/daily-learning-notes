# LIME (Local Interpretable Model-agnostic Explanations)

## What is LIME?

LIME is a model explainability technique that explains individual predictions made by any machine learning model.

Instead of explaining the entire model, LIME focuses on one prediction at a time.

## Why Use LIME?

* Understand individual predictions
* Debug model behavior
* Improve transparency
* Increase user trust

## How LIME Works

1. Select one prediction.
2. Generate similar samples around it.
3. Train a simple interpretable model locally.
4. Explain which features influenced the prediction.

## Advantages

* Works with almost any ML model
* Easy to understand
* Useful for local explanations

## Limitations

* Explains only one prediction at a time
* Results may vary depending on sampled data

## Applications

* Healthcare
* Finance
* Recommendation systems
* NLP models

## What I Learned

* LIME explains individual predictions.
* It creates a simple local model around one prediction.
* It is useful for understanding black-box models.
