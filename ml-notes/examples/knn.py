from sklearn.neighbors import KNeighborsClassifier

# Movie rating similarity example
X = [[1], [2], [3], [6], [7], [8]]
y = ["Bad", "Bad", "Bad", "Good", "Good", "Good"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print(model.predict([[4]]))
