import pandas as pd
def generate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Genera indicadores técnicos y los agrega al DataFrame.

    Args:
        df (pd.DataFrame): DataFrame con los datos base.

    Returns:
        pd.DataFrame: DataFrame con indicadores añadidos.
    """
    # SMA
    for window in [5, 10, 20]:
        df[f'SMA_{window}'] = df['Price'].rolling(window=window).mean()

    # RSI
    delta = df['Price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # Bandas de Bollinger
    df['BB_upper'] = df['SMA_20'] + 2 * df['Price'].rolling(window=20).std()
    df['BB_lower'] = df['SMA_20'] - 2 * df['Price'].rolling(window=20).std()

    # MACD
    ema_12 = df['Price'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Price'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_12 - ema_26
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

    return df
