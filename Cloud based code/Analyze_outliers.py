# analyze_outliers.py

import pandas as pd

# Read the outliers CSV file into a DataFrame
outliers = pd.read_csv('anpr_isolation_forest_outliers.csv')

# Analyze the frequency and context of outliers
outlier_analysis = outliers.groupby(['vehicle_registration']).size().reset_index(name='outlier_count')

# Print the outlier analysis
print("Outlier Analysis:\n", outlier_analysis)

# Save the outlier analysis to a new CSV file
outlier_analysis.to_csv('outlier_analysis.csv', index=False)

print("Outlier analysis complete. Outlier analysis saved to outlier_analysis.csv")