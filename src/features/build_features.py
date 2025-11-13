# src/features/build_features.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_classif

def create_polynomial_features(df, degree=2):
    """
    Create polynomial features up to a specified degree.
    Useful for capturing non-linear relationships between features.
    """
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    poly_features = poly.fit_transform(df)
    poly_feature_names = poly.get_feature_names_out(df.columns)
    
    # Return as DataFrame
    poly_df = pd.DataFrame(poly_features, columns=poly_feature_names)
    return poly_df

def add_interaction_terms(df):
    """
    Add interaction terms between features.
    Example: For feature columns X1, X2, interaction term would be X1*X2.
    """
    interaction_df = pd.DataFrame()
    features = df.columns
    
    for i in range(len(features)):
        for j in range(i + 1, len(features)):
            interaction_df[f"{features[i]}_x_{features[j]}"] = df[features[i]] * df[features[j]]
    
    return interaction_df

def select_best_features(df, target, k=10):
    """
    Select the best 'k' features based on univariate statistical tests (ANOVA F-value).
    """
    from sklearn.feature_selection import SelectKBest, f_classif
    selector = SelectKBest(f_classif, k=k)
    selector.fit(df, target)
    
    # Get the selected features
    selected_columns = df.columns[selector.get_support()]
    return df[selected_columns]

def build_features(df, target):
    """
    Combine various feature engineering steps and return the engineered feature set.
    """
    # Step 1: Create polynomial features
    poly_df = create_polynomial_features(df)
    
    # Step 2: Add interaction terms
    interaction_df = add_interaction_terms(df)
    
    # Step 3: Select the best 'k' features based on statistical tests (e.g., ANOVA)
    best_features_df = select_best_features(df, target, k=10)
    
    # Combine all features
    engineered_features = pd.concat([df, poly_df, interaction_df, best_features_df], axis=1)
    
    return engineered_features


