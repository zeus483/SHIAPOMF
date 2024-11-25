
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data_preprocessing')))
from pipeline import run_pipeline


def test_pipeline_execution():
    input_path = "data/raw/USD_EUR Historical Data.csv"
    output_dir = "data/processed/"

    # Ejecuta el pipeline
    run_pipeline(input_path, output_dir)

    # Verifica que el archivo procesado exista
    files = os.listdir(output_dir)
    processed_files = [f for f in files if f.startswith("processed_data_")]
    assert len(processed_files) > 0, "No se encontró ningún archivo procesado"
