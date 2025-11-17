"""
Data preprocessing utilities.
"""

import pandas as pd
import numpy as np


def encode_features(df):
    """
    Encode categorical features for modeling.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Berkeley admissions dataset
        
    Returns:
    --------
    pd.DataFrame
        Dataset with encoded features
    """
    df_encoded = df.copy()
    
    # Binary encoding
    df_encoded['Admitted'] = (df['Admission'] == 'Accepted').astype(int)
    df_encoded['Gender'] = (df['Sex'] == 'M').astype(int)  # 1=Male, 0=Female
    
    # One-hot encoding for majors
    major_dummies = pd.get_dummies(df['Major'], prefix='Major', drop_first=False)
    df_encoded = pd.concat([df_encoded, major_dummies], axis=1)
    
    return df_encoded


def create_aggregated_stats(df):
    """
    Create aggregated statistics by gender and department.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Berkeley admissions dataset
        
    Returns:
    --------
    pd.DataFrame
        Aggregated statistics
    """
    stats = df.groupby(['Major', 'Sex']).agg({
        'Admission': lambda x: (x == 'Accepted').sum(),
        'Year': 'count'
    }).reset_index()
    
    stats.columns = ['Major', 'Sex', 'Admitted', 'Total']
    stats['Admission_Rate'] = stats['Admitted'] / stats['Total']
    
    return stats