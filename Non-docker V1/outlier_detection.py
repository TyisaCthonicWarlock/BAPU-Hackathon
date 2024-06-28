# outlier_detection.py

from sklearn.ensemble import IsolationForest
import pandas as pd

# Read the clustered CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_clustered.csv')

# Select the features for outlier detection
X = df_cleaned[['latitude', 'longitude', 'vehicle_registration']].dropna()

# Perform outlier detection using Isolation Forest
iso_forest = IsolationForest(contamination=0.01)
df_cleaned['anomaly'] = iso_forest.fit_predict(X)

# Identify the outliers
outliers = df_cleaned[df_cleaned['anomaly'] == -1]

# Save the outliers to a new CSV file
outliers.to_csv('anpr_isolation_forest_outliers.csv', index=False)

print("Isolation Forest outlier detection complete. Outliers saved to anpr_isolation_forest_outliers.csv")