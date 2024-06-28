"""
Step 5: Model Selection and Training
This script selects and trains a RandomForestClassifier using the feature-engineered data.
It saves the trained model to a file using joblib.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the feature-engineered data from the CSV file
anpr_features = pd.read_csv('anpr_features.csv')

# Select features (independent variables) and target variable (dependent variable)
X = anpr_features[['latitude', 'longitude', 'bearing_category']]
y = anpr_features['car_id']

# Split the data into training and testing sets
# test_size=0.2 means 20% of the data will be used for testing, and 80% for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
# n_estimators=100 specifies the number of trees in the forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the trained model to a file using joblib
joblib.dump(clf, 'rf_model.pkl')

# Print a message to indicate the completion of model training
print("Model training complete. Model saved to rf_model.pkl")