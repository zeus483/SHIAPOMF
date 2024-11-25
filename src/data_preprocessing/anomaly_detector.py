import pandas as pd
def detect_anomalies(df: pd.DataFrame, cols: list, threshold: float = 3, method: str = 'remove') -> pd.DataFrame:
    """
    Detecta y maneja anomalías en las columnas especificadas.

    Args:
        df (pd.DataFrame): DataFrame con los datos.
        cols (list): Columnas a analizar para anomalías.
        threshold (float): Umbral de desviación estándar.
        method (str): 'remove' para eliminar, 'impute' para interpolar.

    Returns:
        pd.DataFrame: DataFrame sin anomalías.
    """
    for col in cols:
        mean = df[col].mean()
        std = df[col].std()
        lower_bound = mean - threshold * std
        upper_bound = mean + threshold * std

        if method == 'remove':
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        elif method == 'impute':
            df[col] = df[col].where((df[col] >= lower_bound) & (df[col] <= upper_bound), df[col].interpolate())

    return df
