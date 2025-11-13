import pytest
import pandas as pd
from src.data.preprocess import preprocess_data  # Adjust the import based on your preprocessing function

def test_preprocess_missing_values():
    # Create a sample DataFrame with missing values
    data = pd.DataFrame({
        'feature1': [1000, 2000, None, 4000],
        'feature2': [1, 2, 3, 4],
        'target': [150000, 250000, 350000, 450000]
    })

    # Preprocess the data
    processed_data = preprocess_data(data)

    # Check if missing values were filled (assuming you use median for filling)
    assert processed_data['feature1'].isnull().sum() == 0, "Missing values were not handled correctly"

def test_preprocess_scaling():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'feature1': [1000, 2000, 3000, 4000],
        'feature2': [1, 2, 3, 4],
        'target': [150000, 250000, 350000, 450000]
    })

    # Preprocess the data
    processed_data = preprocess_data(data)
    
    # Check if feature1 is scaled (you can check its mean or standard deviation)
    assert processed_data['feature1'].mean() != 0, "Feature scaling did not work as expected"

