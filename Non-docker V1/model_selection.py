# model_selection.py

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

# Read the feature-engineered CSV file into a DataFrame
df_cleaned = pd.read_csv('anpr_features.csv')

# Select the features and target variable
X = df_cleaned[['hour', 'day_of_week', 'latitude', 'longitude']].dropna()
y = df_cleaned['target']  # Define your target variable

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
rf_model = RandomForestClassifier()

# Train the model
rf_model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(rf_model, 'rf_model.pkl')

print("Model training complete. Model saved to rf_model.pkl")