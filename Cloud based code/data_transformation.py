# data_transformation.py

from geopy.geocoders import Nominatim
import pandas as pd

# Initialize the geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Read the cleaned CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_data_cleaned.csv')

# Function to geocode street names to latitude and longitude
def geocode(street_name):
    try:
        location = geolocator.geocode(street_name)
        return location.latitude, location.longitude
    except:
        return None, None

# Apply the geocode function to the street_name column
df_cleaned['latitude'], df_cleaned['longitude'] = zip(*df_cleaned['street_name'].apply(geocode))

# Save the transformed DataFrame to a new CSV file
df_cleaned.to_csv('anpr_data_transformed.csv', index=False)

print("Data transformation complete. Transformed data saved to anpr_data_transformed.csv")