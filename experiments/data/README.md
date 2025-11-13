# Data Directory

This directory contains the raw and processed data used in the project. The data is the foundation for building machine learning models and making predictions on housing prices.

## Directory Structure

data/
│
└── raw/
└── housing.csv # Raw housing dataset in CSV format


### Dataset Overview

The `housing.csv` dataset contains data on various housing attributes (e.g., area, number of rooms) and their corresponding prices. It is used for regression tasks, where the goal is to predict the price of a house based on the given features.

### Columns:
1. **feature1**: Example feature 1 (e.g., square footage).
2. **feature2**: Example feature 2 (e.g., number of rooms).
3. **feature3**: Example feature 3 (e.g., year built).
4. **feature4**: Example feature 4 (e.g., location).
5. **target**: The target variable, representing house prices (the value we're trying to predict).

### Data Description

This dataset is a small sample containing housing prices, which is ideal for regression tasks. It includes both numerical and categorical features. Missing values have been handled by filling with the median for simplicity.

### Preprocessing Steps

1. **Missing Values**: Any missing values were filled with the median of the respective columns. This is a simple method to handle missing data without dropping any rows.
2. **Scaling**: Features were scaled using **StandardScaler** to standardize the features for better performance with machine learning models.

### How to Use the Data

1. The **raw dataset** is located in the `data/raw/` directory.
2. You can use this dataset for training and evaluating machine learning models, such as regression models for predicting housing prices.

### Licensing

This dataset is used for educational and non-commercial purposes. If you're working with proprietary data, please replace it with the appropriate dataset or refer to the terms of use for the original data source.

---

For more details on how this dataset is used in the model training, refer to the scripts in the `src/` directory.

