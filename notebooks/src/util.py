import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

def missing_report(df):
    # Count of missing values
    missing_count = df.isna().sum()
    
    # Percentage of missing values
    null_average = df.isnull().mean() * 100
    null_average = null_average[null_average > 5]  # Filter > 5%

    print("Columns with more than 5% missing values:\n", null_average)

    return missing_count
def plot_correlation(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.show()
def flag_outlier(df):
    columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
    
    # Drop rows with missing values in selected columns
    z_scores = np.abs(stats.zscore(df[columns].dropna()))
    
    # Flag any row with a Z-score > 3 in any of the columns
    outlier_flags = (z_scores > 3).any(axis=1)
    
    # Create a full-size boolean array to match df's original index
    full_outliers = pd.Series(False, index=df.index)
    full_outliers[df[columns].dropna().index] = outlier_flags

    # Add a new column to the dataframe
    df['Is_Outlier'] = full_outliers

    # Print how many outliers were found per column
    outlier_counts = (z_scores > 3).sum(axis=0)
    print("Outlier count per column:", dict(zip(columns, outlier_counts)))

    return df

     
def incorrect_entries(df):
    for col in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']:
        print(f"{col} < 0: {df[df[col] < 0].shape[0]}")
    if col in ['WS', 'WSgust']:
        print(f"{col} > 50: {df[df[col] > 50].shape[0]}")
def impute_missing(irr_cols , df):
 
    """
    Replace negative values in specified columns with NaN,
    then impute missing values using the column median.
    
    Parameters:
        irr_cols (list): List of columns to process (e.g., ['GHI', 'DNI', 'DHI'])
        df (pd.DataFrame): DataFrame to clean

    Returns:
        pd.DataFrame: Modified DataFrame with imputed values
    """


    # Replace negative values with NaN
    for col in irr_cols:
        df[col] = df[col].mask(df[col] < 0, np.nan)

    # Impute missing values with the median
    for col in irr_cols:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

    return df
def data_analysis(df): 
    # 2. Create a timestamp column based on the index
 df['Timestamp'] = pd.date_range(start='2021-08-09', periods=len(df), freq='1min')

# 3. Set Timestamp as index
 df.set_index('Timestamp', inplace=True)

# 4. Create the plot
 plt.figure(figsize=(14, 8))
 for col in ['GHI', 'DNI', 'DHI', 'Tamb']:  
    plt.plot(df.index, df[col], label=col.upper())

 plt.title('Solar Data Analysis')
 plt.xlabel('Time')
 plt.ylabel('Value')
 plt.legend()
 plt.grid(True)
 plt.tight_layout()
 plt.xticks(rotation=45)
 plt.show()

# 5. Print basic statistics
 print("\nBasic statistics of the main parameters:")
 print(df[['GHI', 'DNI', 'DHI', 'Tamb']].describe())



