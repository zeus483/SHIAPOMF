import pandas as pd
import os
from datetime import datetime

def export_data(df: pd.DataFrame, output_dir: str) -> None:
    """
    Exporta datos procesados a un archivo CSV con timestamp.

    Args:
        df (pd.DataFrame): DataFrame a exportar.
        output_dir (str): Directorio donde guardar el archivo.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = os.path.join(output_dir, f"processed_data_{timestamp}.csv")
    df.to_csv(output_path, index=False)
    print(f"Datos exportados a {output_path}")
