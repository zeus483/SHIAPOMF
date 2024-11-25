import pandas as pd
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica transformaciones y genera nuevas columnas.

    Args:
        df (pd.DataFrame): DataFrame a transformar.

    Returns:
        pd.DataFrame: DataFrame transformado.
    """
    # Normalización (opcional, según modelo)
    price_cols = ['Price', 'Open', 'High', 'Low']
    for col in price_cols:
        df[f'{col}_scaled'] = (df[col] - df[col].mean()) / df[col].std()

    # Generar columnas nuevas
    df['Price_Change'] = df['High'] - df['Low']
    df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']

    return df
