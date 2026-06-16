from sklearn.ensemble import RandomForestClassifier

# Fraud detection simplified dataset
X = [[100], [200], [300], [400], [500], [600]]
y = [0, 0, 0, 1, 1, 1]

model = RandomForestClassifier()
model.fit(X, y)

print(model.predict([[350]]))