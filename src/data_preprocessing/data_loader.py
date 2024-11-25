import pandas as pd
import os


def load_data(file_path: str) -> pd.DataFrame:
    """
    Carga datos desde un archivo CSV y valida las columnas necesarias.

    Args:
        file_path (str): Ruta del archivo a cargar.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    required_columns = ['Date', 'Price', 'Open', 'High', 'Low', 'Change %']
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")

    df = pd.read_csv(file_path, parse_dates=['Date'])

    # Validar columnas esperadas
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"El archivo debe contener las columnas: {required_columns}")

    return df
