# EDA-and-baselines.py

# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('data/housing.csv')

# Show the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Basic Info about the dataset
print(f"\nNumber of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print("\nData types and missing values:\n")
print(df.info())

# Check for missing values
print("\nMissing values in each column:\n")
print(df.isnull().sum())

# Basic Descriptive Statistics
print("\nDescriptive statistics:\n")
print(df.describe())

# Visualizing the distribution of the target variable
sns.histplot(df['target'], kde=True)
plt.title('Target Variable Distribution')
plt.show()

# Visualizing correlation matrix
corr_matrix = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# EDA - Checking outliers for numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[col])
    plt.title(f'Outliers in {col}')
    plt.show()

# Data Preprocessing: Handling Missing Values (if any)
# Let's fill missing values with the median for simplicity
df.fillna(df.median(), inplace=True)

# Feature Engineering: Let's check if we need to scale the features
X = df.drop(columns=['target'])  # Features
y = df['target']  # Target variable

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Baseline Model - Linear Regression
print("\nTraining baseline model: Linear Regression")

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Model Prediction
y_pred_lr = lr_model.predict(X_test)

# Metrics for Linear Regression
mae_lr = mean_absolute_error(y_test, y_pred_lr)
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print(f"\nLinear Regression - MAE: {mae_lr}, MSE: {mse_lr}, R2: {r2_lr}")

# Baseline Model - Random Forest Regressor
print("\nTraining baseline model: Random Forest Regressor")

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Model Prediction
y_pred_rf = rf_model.predict(X_test)

# Metrics for Random Forest Regressor
mae_rf = mean_absolute_error(y_test, y_pred_rf)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print(f"\nRandom Forest Regressor - MAE: {mae_rf}, MSE: {mse_rf}, R2: {r2_rf}")

# Visualizing Predictions vs True Values (Random Forest)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred_rf)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('True vs Predicted (Random Forest Regressor)')
plt.show()
