# test_app.py

import unittest
import requests

class TestANPR(unittest.TestCase):
    def test_prediction(self):
        # Define the URL of the Flask application
        url = 'http://localhost:5000/predict'
        
        # Define the sample input data
        data = {
            'features': [12, 2, 51.5074, -0.1278]  # Replace with actual feature values
        }
        
        # Send a POST request to the Flask application
        response = requests.post(url, json=data)
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response contains a prediction
        self.assertIn('prediction', response.json())

if __name__ == '__main__':
    unittest.main()

# print("Integration testing complete.")