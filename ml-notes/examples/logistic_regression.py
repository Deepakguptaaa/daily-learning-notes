from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

hours = [[5]]

prediction = model.predict(hours)

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")