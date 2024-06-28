import pandas as pd

# Load the cleaned data
anpr_data_cleaned = pd.read_csv('anpr_data_cleaned.csv')

# Print the column names
print(anpr_data_cleaned.columns)