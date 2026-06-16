from sklearn.linear_model import LogisticRegression

# Hours studied vs pass/fail
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[5.5]]))