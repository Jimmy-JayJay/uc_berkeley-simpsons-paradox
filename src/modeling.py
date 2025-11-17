"""
Modeling utilities for logistic regression analysis.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from .preprocessing import encode_features


def run_logistic_regression(df, include_department=True):
    """
    Run logistic regression analysis on Berkeley admissions data.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Berkeley admissions dataset
    include_department : bool
        Whether to include department as a predictor
        
    Returns:
    --------
    dict
        Dictionary containing model results and metrics
    """
    # Encode features
    df_encoded = encode_features(df)
    
    # Prepare target variable
    y = df_encoded['Admitted']
    
    # Prepare features
    if include_department:
        # Full model: Gender + Department
        feature_cols = ['Gender'] + [col for col in df_encoded.columns if col.startswith('Major_')]
        model_name = "Full Model (Gender + Department)"
    else:
        # Naive model: Gender only
        feature_cols = ['Gender']
        model_name = "Naive Model (Gender Only)"
    
    X = df_encoded[feature_cols]
    
    # Fit model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X, y)
    
    # Predictions
    y_pred = model.predict(X)
    y_pred_proba = model.predict_proba(X)[:, 1]
    
    # Calculate metrics
    accuracy = model.score(X, y)
    
    # Gender coefficient and odds ratio
    gender_coef = model.coef_[0][0]
    gender_odds_ratio = np.exp(gender_coef)
    
    # Feature importance (if multiple features)
    if len(feature_cols) > 1:
        feature_importance = pd.DataFrame({
            'Feature': feature_cols,
            'Coefficient': model.coef_[0],
            'Odds_Ratio': np.exp(model.coef_[0])
        }).sort_values('Coefficient', ascending=False)
    else:
        feature_importance = None
    
    # Compile results
    results = {
        'model_name': model_name,
        'model': model,
        'features': feature_cols,
        'accuracy': accuracy,
        'gender_coefficient': gender_coef,
        'gender_odds_ratio': gender_odds_ratio,
        'feature_importance': feature_importance,
        'predictions': y_pred,
        'prediction_probabilities': y_pred_proba,
        'classification_report': classification_report(y, y_pred, 
                                                       target_names=['Rejected', 'Accepted'],
                                                       output_dict=True)
    }
    
    return results


def compare_models(df):
    """
    Compare naive vs full logistic regression models.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Berkeley admissions dataset
        
    Returns:
    --------
    dict
        Comparison results
    """
    # Run both models
    naive_results = run_logistic_regression(df, include_department=False)
    full_results = run_logistic_regression(df, include_department=True)
    
    # Create comparison
    comparison = {
        'naive_model': naive_results,
        'full_model': full_results,
        'gender_coef_change': full_results['gender_coefficient'] - naive_results['gender_coefficient'],
        'accuracy_improvement': full_results['accuracy'] - naive_results['accuracy'],
        'simpsons_paradox_detected': (
            np.sign(naive_results['gender_coefficient']) != np.sign(full_results['gender_coefficient'])
        )
    }
    
    return comparison