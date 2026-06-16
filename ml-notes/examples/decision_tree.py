from sklearn.tree import DecisionTreeClassifier

# Loan approval dataset
# income, credit_score simplified into single feature for learning
X = [[20000], [30000], [40000], [50000], [60000], [70000]]
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[45000]]))