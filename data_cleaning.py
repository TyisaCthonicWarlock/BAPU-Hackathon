import pandas as pd

# Load the collected data
anpr_data = pd.read_csv('anpr_data.csv')
speed_limits_data = pd.read_csv('speed_limits_data.csv')

# Perform data cleaning on anpr_data
anpr_data_cleaned = anpr_data.dropna()

# Save cleaned data
anpr_data_cleaned.to_csv('anpr_data_cleaned.csv', index=False)
speed_limits_data.to_csv('speed_limits_data_cleaned.csv', index=False)

print("Data cleaning complete. Cleaned data saved to anpr_data_cleaned.csv and speed_limits_data_cleaned.csv")