# src/utils/metrics.py
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow

def log_regression_metrics(y_true, y_pred):
    """
    Log common regression metrics: MAE, MSE, and R^2 score to MLflow.
    """
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    # Log metrics to MLflow
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    print(f"MAE: {mae}")
    print(f"MSE: {mse}")
    print(f"R^2: {r2}")
    
    return {"mae": mae, "mse": mse, "r2": r2}

def log_classification_metrics(y_true, y_pred, y_prob=None):
    """
    Log classification metrics: Accuracy, Precision, Recall, F1-Score.
    """
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)

    # Log metrics to MLflow
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1", f1)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}

