import pandas as pd

# Load the transformed CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_data_transformed.csv')

# Print columns to understand structure
print(df_cleaned.columns)

# Create new features based on available data
if 'bearing' in df_cleaned.columns:
    df_cleaned['bearing_category'] = pd.cut(df_cleaned['bearing'], bins=[0, 90, 180, 270, 360], labels=['North', 'East', 'South', 'West'])
else:
    print("Bearing column not found.")

# Handle missing values
df_cleaned['bearing'].fillna(df_cleaned['bearing'].mean(), inplace=True)
df_cleaned['duration'].fillna(df_cleaned['duration'].mean(), inplace=True)

# Save the feature-engineered data to a new CSV file
df_cleaned.to_csv('anpr_features.csv', index=False)

print("Feature engineering complete. Feature-engineered data saved to anpr_features.csv")