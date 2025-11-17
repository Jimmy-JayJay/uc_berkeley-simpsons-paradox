"""
Utility functions.
"""

import pandas as pd
from scipy import stats


def chi_square_test(df, group_by='Sex'):
    """
    Perform chi-square test for independence.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Berkeley admissions dataset
    group_by : str
        Column to group by (default: 'Sex')
        
    Returns:
    --------
    dict
        Test results
    """
    contingency_table = pd.crosstab(df[group_by], df['Admission'])
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    
    results = {
        'chi2_statistic': chi2,
        'p_value': p_value,
        'degrees_of_freedom': dof,
        'significant_at_0.05': p_value < 0.05,
        'contingency_table': contingency_table
    }
    
    return results


def print_summary(results_dict):
    """
    Print formatted summary of analysis results.
    """
    print("\n" + "=" * 70)
    print("BERKELEY ADMISSIONS ANALYSIS - SUMMARY")
    print("=" * 70)
    
    for key, value in results_dict.items():
        if isinstance(value, float):
            print(f"{key}: {value:.4f}")
        else:
            print(f"{key}: {value}")
    
    print("=" * 70 + "\n")