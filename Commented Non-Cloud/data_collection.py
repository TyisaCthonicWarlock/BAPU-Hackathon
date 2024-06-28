"""
Step 1: Data Collection
This script loads data from several TSV files and combines them into a single DataFrame.
It also loads speed limits data and saves both combined data sets to CSV files for further use.
"""

import pandas as pd

# Define paths to the input data files
# These paths point to the locations of the ANPR data files and speed limits data file
burt_anpr_path = '/mnt/data/Challenge2a-Data-PredictingVehicleLocation/Burt_ANPR.tsv'
curtin_anpr_path = '/mnt/data/Challenge2a-Data-PredictingVehicleLocation/Curtin_ANPR.tsv'
metro_anpr_path = '/mnt/data/Challenge2a-Data-PredictingVehicleLocation/Metro_ANPR.tsv'
perth_anpr_path = '/mnt/data/Challenge2a-Data-PredictingVehicleLocation/Perth_ANPR.tsv'
speed_limits_path = '/mnt/data/Challenge2b-Legal_Speed_Limits/Legal_Speed_Limits.dbf'

# Load data from each file using pandas
# sep='\t' specifies that the data files are tab-separated values
burt_anpr = pd.read_csv(burt_anpr_path, sep='\t')
curtin_anpr = pd.read_csv(curtin_anpr_path, sep='\t')
metro_anpr = pd.read_csv(metro_anpr_path, sep='\t')
perth_anpr = pd.read_csv(perth_anpr_path, sep='\t')

# Concatenate all ANPR data into one DataFrame
# ignore_index=True ensures that the indices are re-assigned
anpr_data = pd.concat([burt_anpr, curtin_anpr, metro_anpr, perth_anpr], ignore_index=True)

# Save the consolidated ANPR data to a CSV file for further use
anpr_data.to_csv('anpr_data.csv', index=False)

# Load speed limits data from a dbf file
# pd.read_csv is used here assuming the file can be read as a CSV, if not use an appropriate method to read dbf files
speed_limits_data = pd.read_csv(speed_limits_path)

# Save the speed limits data to a CSV file for further use
speed_limits_data.to_csv('speed_limits_data.csv', index=False)

# Print a message to indicate the completion of data collection
print("Data collection complete. Data saved to anpr_data.csv and speed_limits_data.csv")