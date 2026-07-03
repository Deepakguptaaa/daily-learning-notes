from sklearn.preprocessing import LabelEncoder

fruits = ["Apple", "Banana", "Orange", "Apple", "Banana"]

encoder = LabelEncoder()

encoded = encoder.fit_transform(fruits)

print("Original:", fruits)
print("Encoded:", encoded)