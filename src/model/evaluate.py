# src/model/evaluate.py
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from src.data.make_dataset import prepare_data
from src.features.build_features import build_features

# Load and prepare data
file_path = "data/housing.csv"  # Update this path if necessary
X_train, X_test, y_train, y_test = prepare_data(file_path)

# Feature Engineering
X_train = build_features(X_train, y_train)
X_test = build_features(X_test, y_test)

# Load the model from MLflow (replace the model URI if necessary)
model_uri = "models:/housing_model/1"  # Replace with the correct model version or URI
model = mlflow.sklearn.load_model(model_uri)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")

# Optionally log evaluation metrics to MLflow (for tracking)
mlflow.log_metric("mae", mae)
mlflow.log_metric("mse", mse)

