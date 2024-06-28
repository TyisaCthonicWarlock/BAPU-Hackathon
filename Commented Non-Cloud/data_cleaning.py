"""
Step 2: Data Cleaning
This script cleans the collected data by removing rows with missing car IDs and converting all column names to lowercase.
It saves the cleaned data to new CSV files.
"""

import pandas as pd

# Load the consolidated ANPR data and speed limits data from the CSV files
anpr_data = pd.read_csv('anpr_data.csv')
speed_limits_data = pd.read_csv('speed_limits_data.csv')

# Data Cleaning Steps for ANPR Data
# Remove rows with missing car_id as these are essential for identification
anpr_data_cleaned = anpr_data.dropna(subset=['car_id'])

# Convert column names to lowercase for consistency
anpr_data_cleaned.columns = anpr_data_cleaned.columns.str.lower()

# Save the cleaned data to new CSV files for further use
anpr_data_cleaned.to_csv('anpr_data_cleaned.csv', index=False)
speed_limits_data.to_csv('speed_limits_data_cleaned.csv', index=False)

# Print a message to indicate the completion of data cleaning
print("Data cleaning complete. Cleaned data saved to anpr_data_cleaned.csv and speed_limits_data_cleaned.csv")