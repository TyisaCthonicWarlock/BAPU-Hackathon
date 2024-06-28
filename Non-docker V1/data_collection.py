# data_collection.py

import requests
import pandas as pd

# URL of the API providing the ANPR data
API_URL = 'your_api_url_here'

# Fetch data from the API
response = requests.get(API_URL)
data = response.json()

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('anpr_data.csv', index=False)

print("Data collection complete. Data saved to anpr_data.csv")