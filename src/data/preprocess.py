# src/data/preprocess.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def handle_missing_values(df):
    """
    Handle missing values in the dataset.
    Here, we replace missing numerical values with the median.
    """
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col].fillna(df[col].median(), inplace=True)
    return df

def encode_categorical_features(df):
    """
    Encode categorical features using one-hot encoding.
    """
    df = pd.get_dummies(df, drop_first=True)
    return df

def scale_features(df):
    """
    Scale the features to normalize them for machine learning.
    """
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_scaled

def preprocess_data(raw_data):
    """
    Main function to preprocess the raw data.
    Includes missing value handling, encoding, and feature scaling.
    """
    # Handle missing values
    raw_data = handle_missing_values(raw_data)
    
    # Encode categorical variables
    processed_data = encode_categorical_features(raw_data)
    
    # Scale the features
    processed_data = scale_features(processed_data)
    
    return processed_data

