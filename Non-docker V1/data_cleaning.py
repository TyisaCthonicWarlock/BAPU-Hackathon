# data_cleaning.py

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('anpr_data.csv')

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Fill missing values using forward fill method
df_cleaned = df_cleaned.fillna(method='ffill')

# Convert the timestamp column to datetime format
df_cleaned['timestamp'] = pd.to_datetime(df_cleaned['timestamp'])

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('anpr_data_cleaned.csv', index=False)

print("Data cleaning complete. Cleaned data saved to anpr_data_cleaned.csv")