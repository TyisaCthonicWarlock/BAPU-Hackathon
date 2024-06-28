# pattern_changes_analysis.py

import matplotlib.pyplot as plt
import pandas as pd

# Read the transformed CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_data_transformed.csv')

# Read the rare outliers CSV file into a DataFrame
rare_outliers = pd.read_csv('rare_outliers.csv')

# Filter the data for vehicles identified as rare outliers
pattern_changes = df_cleaned[df_cleaned['vehicle_registration'].isin(rare_outliers['vehicle_registration'])]

# Set the timestamp column as the index
pattern_changes.set_index('timestamp', inplace=True)

# Plot driving patterns during outlier events
for vehicle in pattern_changes['vehicle_registration'].unique():
    vehicle_data = pattern_changes[pattern_changes['vehicle_registration'] == vehicle]
    plt.figure(figsize=(10, 6))
    plt.plot(vehicle_data.index, vehicle_data['latitude'], label='Latitude')
    plt.plot(vehicle_data.index, vehicle_data['longitude'], label='Longitude')
    plt.xlabel('Time')
    plt.ylabel('Coordinates')
    plt.title(f'Driving Patterns for Vehicle: {vehicle}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("Pattern changes analysis complete.")