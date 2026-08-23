import numpy as np
import pandas as pd

def get_summary_stats(df: pd.DataFrame, numeric_cols: list = None) -> pd.DataFrame:
    """
    Generates key statistical metrics for specified numeric features.
    """
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    return df[numeric_cols].describe().T[['count', 'mean', 'std', 'min', '50%', 'max']]