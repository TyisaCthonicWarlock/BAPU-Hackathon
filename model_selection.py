import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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

# Initialize and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save the trained model
with open('rf_model.pkl', 'wb') as model_file:
    pickle.dump(rf_model, model_file)

print("Model training complete. Model saved to rf_model.pkl")