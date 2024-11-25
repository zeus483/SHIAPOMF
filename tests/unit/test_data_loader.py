import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data_preprocessing')))
from data_loader import load_data

def test_load_data_csv():
    #prueba con un archivo valido
    df = load_data('data/raw/USD_EUR Historical Data.csv')
    assert not df.empty, "El df no debe estar vacio"
    assert "Date" in df.columns, "El df debe tener una columna date"