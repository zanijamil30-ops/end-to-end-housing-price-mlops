# src/data/make_dataset.py
import pandas as pd
from sklearn.model_selection import train_test_split
from src.data.preprocess import preprocess_data

def load_data(file_path):
    """
    Load the dataset from the provided CSV file.
    """
    df = pd.read_csv(file_path)
    return df

def create_train_test_split(df, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    """
    X = df.drop(columns=["target"])  # Assume "target" is the column to predict
    y = df["target"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    return X_train, X_test, y_train, y_test

def save_split_data(X_train, X_test, y_train, y_test):
    """
    Save the train/test splits as CSVs or pickle files for future use.
    """
    X_train.to_csv("data/X_train.csv", index=False)
    X_test.to_csv("data/X_test.csv", index=False)
    y_train.to_csv("data/y_train.csv", index=False)
    y_test.to_csv("data/y_test.csv", index=False)

def prepare_data(file_path):
    """
    Full pipeline for preparing data: loading, preprocessing, splitting, and saving.
    """
    # Load raw data
    df = load_data(file_path)
    
    # Preprocess the raw data
    processed_data = preprocess_data(df)
    
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = create_train_test_split(processed_data)
    
    # Optionally, save the data splits
    save_split_data(X_train, X_test, y_train, y_test)
    
    return X_train, X_test, y_train, y_test

