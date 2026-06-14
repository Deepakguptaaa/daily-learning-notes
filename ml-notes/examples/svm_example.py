from sklearn.svm import SVC

X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

model = SVC()
model.fit(X, y)

print(model.predict([[5]]))