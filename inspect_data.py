import pandas as pd

# Load the CSV file into a DataFrame
vehicle_data = pd.read_csv('anpr_data.csv')

# Print the first few rows and column names
print(vehicle_data.head())
print(vehicle_data.columns)