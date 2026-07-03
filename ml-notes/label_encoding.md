# Label Encoding

## What is Label Encoding?

Label Encoding converts categorical values into numerical values.

Machine learning algorithms require numerical input, so categorical data must often be encoded.

## Example

Original:

* Red
* Blue
* Green

Encoded:

* Red → 2
* Blue → 0
* Green → 1

## Advantages

* Simple to implement
* Saves memory
* Useful for ordinal data

## Limitations

* May introduce an unintended order between categories.
* Not suitable for most nominal categorical features.

## Applications

* Customer datasets
* Product categories
* Medical records
* Survey responses

## What I Learned

* Label Encoding converts text labels into numbers.
* It is useful when categories have a natural order.
* For unordered categories, One-Hot Encoding is often a better choice.
