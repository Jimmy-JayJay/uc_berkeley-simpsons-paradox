"""
Visualization utilities.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")


def plot_admission_rates_by_gender(df, save_path=None):
    """
    Plot overall admission rates by gender.
    """
    stats = df.groupby('Sex')['Admission'].apply(
        lambda x: (x == 'Accepted').mean()
    )
    
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(['Female', 'Male'], stats.values, color=['#FF6B6B', '#4ECDC4'])
    
    ax.set_title('Overall Admission Rates by Gender', fontsize=14, fontweight='bold')
    ax.set_ylabel('Admission Rate', fontsize=12)
    ax.set_ylim(0, 1)
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1%}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax


def plot_department_comparison(df, save_path=None):
    """
    Plot admission rates by department and gender.
    """
    dept_stats = df.pivot_table(
        values='Admission',
        index='Major',
        columns='Sex',
        aggfunc=lambda x: (x == 'Accepted').mean()
    )
    
    fig, ax = plt.subplots(figsize=(12, 6))
    dept_stats.plot(kind='bar', ax=ax, color=['#FF6B6B', '#4ECDC4'])
    
    ax.set_title('Admission Rates by Department and Gender', fontsize=14, fontweight='bold')
    ax.set_ylabel('Admission Rate', fontsize=12)
    ax.set_xlabel('Department', fontsize=12)
    ax.legend(['Female', 'Male'], title='Gender')
    ax.grid(axis='y', alpha=0.3)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax