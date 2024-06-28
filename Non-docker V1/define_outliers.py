# define_outliers.py

from scipy.stats import zscore
import pandas as pd

# Read the clustered CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_clustered.csv')

# Calculate Z-scores for the vehicle registrations
df_cleaned['zscore'] = zscore(df_cleaned['vehicle_registration'])

# Identify outliers (Z-score > 3)
outliers = df_cleaned[df_cleaned['zscore'] > 3]

# Save the outliers to a new CSV file
outliers.to_csv('anpr_outliers.csv', index=False)

print("Outlier detection complete. Outliers saved to anpr_outliers.csv")