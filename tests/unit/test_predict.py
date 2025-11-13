import pytest
import joblib
import numpy as np
from src.model.predict import predict_price  # Adjust based on your prediction function

def test_predict_price():
    # Load the saved model (assuming it's stored as 'model.pkl')
    model = joblib.load('models/model.pkl')
    
    # Create a sample input (a row of data) for prediction
    sample_input = np.array([[2000, 3, 1]])  # Example: [square footage, number of rooms, year built]

    # Predict using the model
    prediction = predict_price(model, sample_input)
    
    # Check if the prediction is a scalar (single value)
    assert isinstance(prediction, (int, float)), "Prediction should be a numeric value"
    
    # Optionally, check if the prediction is within a reasonable range (adjust the range)
    assert 100000 <= prediction <= 1000000, "Prediction out of expected range"

