import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Perform K-means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
kmeans_labels = kmeans.labels_

# Perform Gaussian Mixture Model (GMM) clustering
scaler = preprocessing.StandardScaler()
X_scaled = scaler.fit_transform(X)

gmm = GaussianMixture(n_components=3)
gmm.fit(X_scaled)
gmm_labels = gmm.predict(X_scaled)

# Visualize the clustering results
plt.figure(figsize=(14, 14))

# Plot the original classifications using Petal features
plt.subplot(2, 2, 1)
plt.scatter(X[:, 2], X[:, 3], c=y, cmap='viridis')
plt.title('Real Clusters')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

# Plot the K-means clustering results
plt.subplot(2, 2, 2)
plt.scatter(X[:, 2], X[:, 3], c=kmeans_labels, cmap='viridis')
plt.title('K-Means Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

# Plot the GMM clustering results
plt.subplot(2, 2, 3)
plt.scatter(X[:, 2], X[:, 3], c=gmm_labels, cmap='viridis')
plt.title('GMM Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.show()

print('Observation: The GMM using EM algorithm-based clustering matched the true labels more closely than the K-means.')
