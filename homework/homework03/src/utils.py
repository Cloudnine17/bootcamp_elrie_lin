import pandas as pd

def get_summary_stats(df: pd.DataFrame, group_col: str = None, numeric_col: str = None) -> pd.DataFrame:
    """
    Generate summary statistics for a DataFrame.
    Optionally performs a groupby aggregation if group_col and numeric_col are provided.
    """
    if group_col and numeric_col:
        summary = df.groupby(group_col)[numeric_col].agg(['count', 'mean', 'std', 'min', 'max']).reset_index()
    else:
        summary = df.describe()
    return summary
