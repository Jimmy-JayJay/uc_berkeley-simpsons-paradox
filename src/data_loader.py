"""
Data loading utilities for Berkeley admissions dataset.
"""

import pandas as pd
from pathlib import Path


def load_berkeley_data(filepath='data/raw/berkeley.csv'):
    """
    Load the Berkeley admissions dataset.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataset with columns: Year, Major, Sex, Admission
    """
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Successfully loaded {len(df):,} applications")
        return df
    except FileNotFoundError:
        print(f"✗ Error: File not found at {filepath}")
        return None


def get_basic_stats(df):
    """
    Get basic statistics about the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Berkeley admissions dataset
        
    Returns:
    --------
    dict
        Dictionary containing basic statistics
    """
    stats = {
        'total_applications': len(df),
        'departments': df['Major'].nunique(),
        'male_applicants': (df['Sex'] == 'M').sum(),
        'female_applicants': (df['Sex'] == 'F').sum(),
        'total_admitted': (df['Admission'] == 'Accepted').sum(),
        'total_rejected': (df['Admission'] == 'Rejected').sum(),
        'overall_admission_rate': (df['Admission'] == 'Accepted').mean()
    }
    return stats
