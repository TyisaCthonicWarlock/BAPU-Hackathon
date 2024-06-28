"""
Step 6: Model Evaluation
This script evaluates the performance of the trained model using accuracy score and classification report.
It prints the evaluation metrics to the console.
"""

import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the feature-engineered data from the CSV file and the trained model from the file
anpr_features = pd.read_csv('anpr_features.csv')
clf = joblib.load('rf_model.pkl')

# Select features and target variable
X = anpr_features[['latitude', 'longitude', 'bearing_category']]
y = anpr_features['car_id']

# Split the data into training and testing sets
# test_size=0.2 means 20% of the data will be used for testing, and 80% for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predict on the test set using the trained model
y_pred = clf.predict(X_test)

# Evaluate the model using accuracy score and classification report
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print the evaluation metrics to the console
print(f"Model Accuracy: {accuracy}")
print("Classification Report:")
print(report)