import pandas as pd

# Read the feature-engineered CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_features.csv')

# Print columns to understand structure
print(df_cleaned.columns)

# Check for missing values
print(df_cleaned.isnull().sum())