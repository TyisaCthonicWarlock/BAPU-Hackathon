import os

# Define the directory paths
vehicle_data_dir = r'C:\Users\tfel4\OneDrive\Documents\2024\WAPOL Hackathon\Challenge2a-Data-PredictingVehicleLocation'
speed_limits_dir = r'C:\Users\tfel4\OneDrive\Documents\2024\WAPOL Hackathon\Challenge2b-Legal_Speed_Limits'

# List files in the vehicle data directory
print("Files in vehicle data directory:")
for file in os.listdir(vehicle_data_dir):
    print(f"{vehicle_data_dir}\\{file}")

# List files in the speed limits directory
print("Files in speed limits directory:")
for file in os.listdir(speed_limits_dir):
    print(f"{speed_limits_dir}\\{file}")