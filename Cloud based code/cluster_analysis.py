# cluster_analysis.py

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

# Read the transformed CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_data_transformed.csv')

# Select the features for clustering
X = df_cleaned[['latitude', 'longitude']].dropna()

# Perform K-means clustering
kmeans = KMeans(n_clusters=5)
df_cleaned['cluster'] = kmeans.fit_predict(X)

# Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['longitude'], df_cleaned['latitude'], c=df_cleaned['cluster'], cmap='viridis', marker='o', s=10)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Vehicle Clusters')
plt.show()

# Save the clustered DataFrame to a new CSV file
df_cleaned.to_csv('anpr_clustered.csv', index=False)

print("Cluster analysis complete. Clustered data saved to anpr_clustered.csv")