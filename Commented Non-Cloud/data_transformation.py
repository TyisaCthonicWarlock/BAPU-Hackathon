"""
Step 3: Data Transformation
This script transforms the cleaned data by extracting the date and time from the timestamp column, if it exists.
It saves the transformed data to a new CSV file.
"""

import pandas as pd

# Load the cleaned ANPR data from the CSV file
anpr_data_cleaned = pd.read_csv('anpr_data_cleaned.csv')

# Check if 'timestamp' column exists in the data
if 'timestamp' in anpr_data_cleaned.columns:
    # Convert 'timestamp' column to datetime format and create separate 'date' and 'time' columns
    anpr_data_cleaned['date'] = pd.to_datetime(anpr_data_cleaned['timestamp']).dt.date
    anpr_data_cleaned['time'] = pd.to_datetime(anpr_data_cleaned['timestamp']).dt.time

# Save the transformed data to a new CSV file for further use
anpr_data_cleaned.to_csv('anpr_data_transformed.csv', index=False)

# Print a message to indicate the completion of data transformation
print("Data transformation complete. Transformed data saved to anpr_data_transformed.csv")