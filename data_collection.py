import pandas as pd

# Paths to the data files
burt_anpr_path = 'C:/Users/tfel4/OneDrive/Documents/2024/WAPOL Hackathon/Challenge2a-Data-PredictingVehicleLocation/Burt_ANPR.tsv'
curtin_anpr_path = 'C:/Users/tfel4/OneDrive/Documents/2024/WAPOL Hackathon/Challenge2a-Data-PredictingVehicleLocation/Curtin_ANPR.tsv'
metro_anpr_path = 'C:/Users/tfel4/OneDrive/Documents/2024/WAPOL Hackathon/Challenge2a-Data-PredictingVehicleLocation/Metro_ANPR.tsv'
perth_anpr_path = 'C:/Users/tfel4/OneDrive/Documents/2024/WAPOL Hackathon/Challenge2a-Data-PredictingVehicleLocation/Perth_ANPR.tsv'
speed_limits_path = 'C:/Users/tfel4/OneDrive/Documents/2024/WAPOL Hackathon/Challenge2b-Legal_Speed_Limits/Legal_Speed_Limits.dbf'

# Read the data files
burt_anpr = pd.read_csv(burt_anpr_path, sep='\t')
curtin_anpr = pd.read_csv(curtin_anpr_path, sep='\t')
metro_anpr = pd.read_csv(metro_anpr_path, sep='\t')
perth_anpr = pd.read_csv(perth_anpr_path, sep='\t')

# For the speed limits data, we need to use geopandas
import geopandas as gpd
speed_limits = gpd.read_file(speed_limits_path)

# Combine all ANPR data into one DataFrame
anpr_data = pd.concat([burt_anpr, curtin_anpr, metro_anpr, perth_anpr])

# Save the combined data to CSV
anpr_data.to_csv('anpr_data.csv', index=False)
speed_limits.to_csv('speed_limits_data.csv', index=False)

print("Data collection complete. Data saved to anpr_data.csv and speed_limits_data.csv")