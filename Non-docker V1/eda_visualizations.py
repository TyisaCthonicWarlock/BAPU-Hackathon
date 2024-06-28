# eda_visualizations.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read the transformed CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_data_transformed.csv')

# Plot the number of vehicles detected over time
plt.figure(figsize=(10, 6))
plt.plot(df_cleaned['timestamp'], df_cleaned['vehicle_registration'], marker='o', linestyle='-', markersize=2)
plt.xlabel('Time')
plt.ylabel('Number of Vehicles')
plt.title('Vehicle Detection Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create a heatmap of vehicle counts by latitude and longitude
heatmap_data = df_cleaned.pivot_table(index='latitude', columns='longitude', values='vehicle_registration', aggfunc='count')
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='viridis')
plt.title('Heatmap of Vehicle Counts by Latitude and Longitude')
plt.show()