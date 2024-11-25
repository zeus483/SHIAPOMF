from data_loader import load_data
from data_cleaner import clean_data
from data_transformer import transform_data
from anomaly_detector import detect_anomalies
from indicator_generator import generate_indicators
from exporter import export_data

def run_pipeline(input_path: str, output_dir: str) -> None:
    """
    Ejecuta el pipeline completo de preprocesamiento de datos.

    Args:
        input_path (str): Ruta del archivo de entrada.
        output_dir (str): Directorio de salida para datos procesados.
    """
    df = load_data(input_path)
    df = clean_data(df)
    df = transform_data(df)
    df = detect_anomalies(df, cols=['Price', 'Change %'], method='remove')
    df = generate_indicators(df)
    export_data(df, output_dir)

# Ejecución
if __name__ == "__main__":
    run_pipeline("data/raw/USD_EUR Historical Data.csv", "data/processed/")
