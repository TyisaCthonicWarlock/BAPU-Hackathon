# identify_high_adrenaline.py

import pandas as pd

# Read the outlier analysis CSV file into a DataFrame
outlier_analysis = pd.read_csv('outlier_analysis.csv')

# Define the threshold for identifying high adrenaline instances
threshold = 5

# Filter outliers that occur infrequently (less than the threshold)
rare_outliers = outlier_analysis[outlier_analysis['outlier_count'] < threshold]

# Save the rare outliers to a new CSV file
rare_outliers.to_csv('rare_outliers.csv', index=False)

print("High adrenaline instance detection complete. Rare outliers saved to rare_outliers.csv")