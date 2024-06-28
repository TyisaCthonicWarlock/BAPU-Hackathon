"""
Step 4: Feature Engineering
This script creates new features, such as categorizing the bearing into compass directions.
It saves the feature-engineered data to a new CSV file.
"""

import pandas as pd

# Load the transformed ANPR data from the CSV file
anpr_data_transformed = pd.read_csv('anpr_data_transformed.csv')

# Define a function to categorize bearing into compass directions
def categorize_bearing(bearing):
    if bearing >= 0 and bearing < 90:
        return 'NE'  # North-East
    elif bearing >= 90 and bearing < 180:
        return 'SE'  # South-East
    elif bearing >= 180 and bearing < 270:
        return 'SW'  # South-West
    else:
        return 'NW'  # North-West

# Apply the function to create a new column 'bearing_category' if 'bearing' column exists
if 'bearing' in anpr_data_transformed.columns:
    anpr_data_transformed['bearing_category'] = anpr_data_transformed['bearing'].apply(categorize_bearing)

# Save the feature-engineered data to a new CSV file for further use
anpr_data_transformed.to_csv('anpr_features.csv', index=False)

# Print a message to indicate the completion of feature engineering
print("Feature engineering complete. Feature-engineered data saved to anpr_features.csv")