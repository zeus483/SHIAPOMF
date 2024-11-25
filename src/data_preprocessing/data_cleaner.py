import pandas as pd
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia los datos eliminando duplicados y asegurando consistencia.

    Args:
        df (pd.DataFrame): DataFrame a limpiar.

    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    # Eliminar duplicados
    df = df.drop_duplicates()
    try:
        df.drop(columns=['Vol.'], inplace=True)
    except:
        print("no existe la columna Vol.")
    # Asegurarse de que las columnas numéricas sean float64
    numeric_cols = ['Price', 'Open', 'High', 'Low', 'Change %']
    df["Change %"] = df["Change %"].str.replace("%", "").astype('float64')
    for col in numeric_cols:
        df[col] = df[col].astype('float64')

    return df
