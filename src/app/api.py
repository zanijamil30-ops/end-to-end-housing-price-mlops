# src/app/api.py
import mlflow
import json
import numpy as np
from fastapi.responses import JSONResponse

# Assuming a model is already logged in MLflow
MODEL_URI = "models:/housing_model/1"  # You can adjust this path according to your model

# Health check function
def health_check():
    """
    Basic health check response for the app.
    """
    return {"status": "healthy"}

# Prediction function
async def predict(input_data: dict):
    """
    Perform prediction using the loaded MLflow model
    """
    try:
        # Load the MLflow model (this can be done once at the start for efficiency)
        model = mlflow.sklearn.load_model(MODEL_URI)

        # Prepare the input data (example: convert to numpy array if needed)
        features = np.array(input_data["features"]).reshape(1, -1)  # Assuming features come as a list

        # Predict
        prediction = model.predict(features)
        return {"prediction": prediction.tolist()}  # Convert to list for JSON serializability
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

