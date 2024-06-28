import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load the feature-engineered data
df_cleaned = pd.read_csv('anpr_features.csv')

# Print columns to understand structure
print(df_cleaned.columns)

# Define feature columns and target column
X = df_cleaned[['bearing', 'duration', 'bearing_category']]  # Add more features as needed
y = df_cleaned['car_id']

# Convert categorical features to numerical
X = pd.get_dummies(X, columns=['bearing_category'], drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained model
with open('rf_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy}")
print("Classification Report:")
print(report)