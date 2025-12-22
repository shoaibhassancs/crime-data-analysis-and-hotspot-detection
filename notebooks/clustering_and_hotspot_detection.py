import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/karachi_crime_2020_2025_one_hot_encoded.csv')
le_df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/karachi_crime_2020_2025_label_encoded.csv')
raw_df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/karachi_crime_2020_2025_cleaned.csv')

# -----------------------------
# Feature selection for clustering
# -----------------------------
features = ['LATITUDE', 'LONGITUDE'] 
X = df[features] # new df with only selected features

# -----------------------------
# Choosing Optimal K
# -----------------------------
# - Elbow Method: Identify where adding more clusters stops giving meaningful improvement
inertia = [] # how tightly grouped the data points are within each cluster
K = range(1, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_) # Store the inertia value for this k

plt.figure()
plt.plot(K, inertia, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()
plt.savefig('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/visuals/elbow_method.png')

# - Silhouette Analysis: Validate the quality and separation of clusters
X_sample = X.sample(n=3000, random_state=42) # Sample data for efficiency

silhouette_scores = []
K_sil = range(2, 11) # silhouette score cannot be calculated for k=1, minimum clusters required is 2

for k in K_sil:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_sample) # Fits the model and Returns cluster labels for each point
    silhouette_scores.append(silhouette_score(X_sample, labels)) # recognise which points are same cluster and which are in different clusters and store the score

plt.figure()
plt.plot(K_sil, silhouette_scores, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Analysis')
plt.show()
plt.savefig('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/visuals/silhouette_analysis.png')

# -----------------------------
# Clustering
# -----------------------------
optimal_k = 4  # determined from previous analysis
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42) # Fit K-Means with chosen k
df['cluster'] = kmeans_final.fit_predict(X) # Assign cluster labels to each crime record
df['cluster'] = df['cluster'].astype('category')

# -----------------------------
# Cluster Analysis
# -----------------------------
# Count number of incidents per cluster (crime frequency)
cluster_counts = df['cluster'].value_counts().sort_index().reset_index()
cluster_counts.columns = ['cluster', 'crime_count']

# Calculate cluster centroids (hotspot centers)
centroids = kmeans_final.cluster_centers_
centroid_df = pd.DataFrame(centroids, columns=features)
centroid_df['cluster'] = centroid_df.index
centroid_df = centroid_df[['cluster', 'LATITUDE', 'LONGITUDE']]

# Merge counts with centroids
cluster_analysis = centroid_df.merge(cluster_counts, on='cluster')

# Rank clusters by crime density (hotspot intensity)
cluster_analysis = cluster_analysis.sort_values(by='crime_count', ascending=False)

# Add crime percentage column
total_crimes = len(df)
cluster_analysis['crime_percentage'] = (cluster_analysis['crime_count'] / total_crimes) * 100

# Reset index for clean display
cluster_analysis = cluster_analysis.reset_index(drop=True)

# Display final cluster analysis
print(cluster_analysis)

# -----------------------------
# Visualization
# -----------------------------
plt.figure(figsize=(10, 8))

# Plot all crimes colored by cluster
scatter = plt.scatter(
    df['LONGITUDE'], 
    df['LATITUDE'], 
    c=df['cluster'].cat.codes,  # numeric codes for clusters
    cmap='viridis',             # colormap
    alpha=0.5                   # transparency
)
plt.colorbar(scatter, label='Cluster')  # add color legend

# Plot cluster centroids (hotspot centers)
plt.scatter(
    cluster_analysis['LONGITUDE'], 
    cluster_analysis['LATITUDE'], 
    s=200,
    c='red',
    marker='X',
    label='Hotspot Centroid'
)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Clusters and Hotspots in Karachi')
plt.legend()
plt.show()

# Save figure
plt.savefig('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/visuals/crime_clusters_hotspots.png')

# -----------------------------
# Interpretation
# -----------------------------
# Label clusters as High / Medium / Low risk
q1, q2, q3 = cluster_analysis['crime_percentage'].quantile([0.25, 0.5, 0.75]) # quantile is used to divide data into intervals with equal probabilities

def assign_risk_quantile(crime_percentage):
    if crime_percentage >= q3:
        return 'High'
    elif crime_percentage >= q2:
        return 'Medium'
    elif crime_percentage >= q1:
        return 'Low'
    else:
        return 'Very Low'


cluster_analysis['risk_level'] = cluster_analysis['crime_percentage'].apply(assign_risk_quantile)

# Copy cluster assignments row-by-row
le_df['cluster'] = df['cluster'].values 
raw_df[['TOWN', 'SUBDIVISION']].head()

# Attach readable names to le_df
le_df['TOWN_NAME'] = raw_df['TOWN'].values
le_df['SUBDIVISION_NAME'] = raw_df['SUBDIVISION'].values

le_df[['TOWN_NAME', 'SUBDIVISION_NAME', 'cluster']].head()

# Link clusters back to towns / subdivisions
town_cluster_summary = (
    le_df
    .groupby(['cluster', 'TOWN_NAME']) # Groups crimes by cluster + town
    .size() # Counts number of crimes in each group
    .reset_index(name='crime_count') # Resets index and names the count column
    .sort_values(['cluster', 'crime_count'], ascending=[True, False]) # Sorts by cluster and then by crime count within each cluster
)
town_cluster_summary.head(10)

# top towns per cluster
top_towns_per_cluster = (
    town_cluster_summary
    .groupby('cluster')
    .head(3)
    .reset_index(drop=True)
)
top_towns_per_cluster

# Extract actionable insights (where crime concentrates)
town_cluster_summary = town_cluster_summary.merge(
    cluster_analysis[['cluster', 'risk_level']],
    on='cluster',
    how='left'
) # Merge risk levels into town summary
town_cluster_summary.head(10)

# Focus on high-risk clusters only
high_risk_towns = town_cluster_summary[
    town_cluster_summary['risk_level'] == 'High'
]
high_risk_towns.head(10)

# Extract top towns in high-risk areas
top_high_risk_towns = (
    high_risk_towns
    .sort_values('crime_count', ascending=False)
    .head(10)
)
top_high_risk_towns

# -----------------------------
# Save Outputs
# -----------------------------
# Save clustered dataset
le_df.to_csv(
    '/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/karachi_crime_2020_2025_with_clusters.csv',
    index=False
)

# Save hotspot summary
cluster_analysis.to_csv(
    '/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/karachi_crime_2020_2025_cluster_summary.csv',
    index=False
)

top_towns_per_cluster.to_csv(
    '/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/top_towns_per_cluster.csv',
    index=False
)