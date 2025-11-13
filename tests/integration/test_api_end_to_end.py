import pytest
from fastapi.testclient import TestClient
from src.app.main import app  # Adjust based on your FastAPI app

client = TestClient(app)

def test_predict_api():
    # Sample input for the API
    sample_input = {
        "feature1": 2000,  # square footage
        "feature2": 3,     # number of rooms
        "feature3": 1,     # year built
    }

    # Make a POST request to the /predict endpoint
    response = client.post("/predict", json=sample_input)
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check if the response contains a 'prediction' key
    assert "prediction" in response.json(), "Response doesn't contain 'prediction' key"
    
    # Optionally, check the range of the prediction (adjust the range based on your model's output)
    prediction = response.json()["prediction"]
    assert 100000 <= prediction <= 1000000, f"Prediction out of expected range: {prediction}"

