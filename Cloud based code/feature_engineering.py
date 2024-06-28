# feature_engineering.py

import pandas as pd

# Read the transformed CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_data_transformed.csv')

# Create new features based on driving patterns, outlier frequency, time of day, and location data
df_cleaned['hour'] = pd.to_datetime(df_cleaned['timestamp']).dt.hour
df_cleaned['day_of_week'] = pd.to_datetime(df_cleaned['timestamp']).dt.dayofweek

# Save the feature-engineered data to a new CSV file
df_cleaned.to_csv('anpr_features.csv', index=False)

print("Feature engineering complete. Feature-engineered data saved to anpr_features.csv")