# training_evaluation.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
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

# Load the trained model from the file
rf_model = joblib.load('rf_model.pkl')

# Make predictions on the test data
y_pred = rf_model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Print the evaluation metrics
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')

print("Model evaluation complete.")