# src/model/train.py
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from src.data.make_dataset import prepare_data
from src.features.build_features import build_features

# Load and prepare data
file_path = "data/housing.csv"  # Update this path if necessary
X_train, X_test, y_train, y_test = prepare_data(file_path)

# Feature Engineering
X_train = build_features(X_train, y_train)
X_test = build_features(X_test, y_test)

# MLflow Experiment Tracking
mlflow.start_run()

# Log model parameters and other info
mlflow.log_param("model", "RandomForestRegressor")
mlflow.log_param("n_estimators", 100)
mlflow.log_param("max_depth", 10)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Log the trained model
mlflow.sklearn.log_model(model, "model")

# Log performance metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

mlflow.log_metric("mae", mae)
mlflow.log_metric("mse", mse)

# End the MLflow run
mlflow.end_run()

print("Training complete. Metrics and model logged to MLflow.")

