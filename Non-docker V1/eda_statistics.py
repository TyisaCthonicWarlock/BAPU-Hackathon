# eda_statistics.py

import pandas as pd

# Read the transformed CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_data_transformed.csv')

# Calculate basic statistics
stats = df_cleaned.describe()

# Print the statistics
print("Descriptive Statistics:\n", stats)