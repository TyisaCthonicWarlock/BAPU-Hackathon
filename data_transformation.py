import pandas as pd

# Load the cleaned data
anpr_data_cleaned = pd.read_csv('anpr_data_cleaned.csv')

# Print columns to understand structure
print(anpr_data_cleaned.columns)

# No timestamp column, so no date transformation
# Apply other necessary transformations (if any)

# Save the transformed data
anpr_data_cleaned.to_csv('anpr_data_transformed.csv', index=False)

print("Data transformation complete. Transformed data saved to anpr_data_transformed.csv")