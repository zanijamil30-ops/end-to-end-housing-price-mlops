# src/model/predict.py
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from src.features.build_features import build_features

def load_model(model_uri="models:/housing_model/1"):
    """
    Load the model from MLflow for inference.
    """
    return mlflow.sklearn.load_model(model_uri)

def predict(input_data):
    """
    Predict using the loaded model.
    Assumes input_data is a dict with feature values.
    """
    # Convert the input_data to a pandas DataFrame (you may need to preprocess it first)
    input_df = pd.DataFrame([input_data])

    # Feature engineering
    input_df = build_features(input_df, None)  # Assuming no target variable in inference

    # Load the model
    model = load_model()

    # Make prediction
    prediction = model.predict(input_df)

    return prediction.tolist()  # Return the result as a list for easier JSON serialization

if __name__ == "__main__":
    # Example of how to use the script for inference
    example_input = {
        "feature1": 5.1,
        "feature2": 3.5,
        "feature3": 1.4,
        "feature4": 0.2
    }

    prediction = predict(example_input)
    print(f"Prediction: {prediction}")

