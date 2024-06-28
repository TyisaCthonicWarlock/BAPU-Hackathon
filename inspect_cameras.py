import pandas as pd

# Define file paths for camera data
camera_data_paths = {
    "Burt_Cameras": r'C:\Users\tfel4\OneDrive\Documents\2024\WAPOL Hackathon\Challenge2a-Data-PredictingVehicleLocation\Burt_Cameras.tsv',
    "Curtin_Cameras": r'C:\Users\tfel4\OneDrive\Documents\2024\WAPOL Hackathon\Challenge2a-Data-PredictingVehicleLocation\Curtin_Cameras.tsv',
    "Metro_Cameras": r'C:\Users\tfel4\OneDrive\Documents\2024\WAPOL Hackathon\Challenge2a-Data-PredictingVehicleLocation\Metro_Cameras.tsv',
    "Perth_Cameras": r'C:\Users\tfel4\OneDrive\Documents\2024\WAPOL Hackathon\Challenge2a-Data-PredictingVehicleLocation\Perth_Cameras.tsv'
}

# Load and inspect each camera data file
for name, path in camera_data_paths.items():
    camera_data = pd.read_csv(path, sep='\t')
    print(f"{name} data head:")
    print(camera_data.head())
    print(camera_data.columns)
    print("\n")