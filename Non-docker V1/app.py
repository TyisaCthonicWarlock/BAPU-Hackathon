# app.py

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model from the file
model = joblib.load('rf_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json(force=True)
    
    # Extract features from the data
    features = [data['features']]
    
    # Make a prediction using the model
    prediction = model.predict(features)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

print("Flask application running. Access it at http://localhost:5000")