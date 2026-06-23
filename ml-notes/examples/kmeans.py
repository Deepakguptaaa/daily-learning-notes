from sklearn.cluster import KMeans

# Sample customer data (Age, Spending Score)
X = [
    [20, 30],
    [22, 35],
    [25, 40],
    [45, 80],
    [50, 85],
    [55, 90]
]

model = KMeans(n_clusters=2, random_state=42)
model.fit(X)

print("Cluster Labels:")
print(model.labels_)

print("\nCluster Centers:")
print(model.cluster_centers_)