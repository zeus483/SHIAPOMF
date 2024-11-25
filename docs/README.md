# Pipeline de Preprocesamiento de Datos

Este pipeline realiza el preprocesamiento de los datos de mercado para preparar un conjunto de datos limpio y enriquecido con indicadores técnicos. Está diseñado de forma modular, permitiendo su mantenimiento y pruebas fáciles.

## Pasos del Pipeline

### 1. Carga de Datos
- Lee archivos CSV desde `data/raw`.
- Valida la presencia de las columnas necesarias: `Date`, `Price`, `Open`, `High`, `Low`, `Change %`.
- Convierte automáticamente la columna `Date` a formato `datetime`.

### 2. Limpieza de Datos
- Elimina duplicados.
- Verifica la ausencia de valores nulos.
- Asegura que las columnas numéricas (`Price`, `Open`, `High`, `Low`, `Change %`) estén en formato `float64`.
- Elimina la columna `Vol.` si existe
### 3. Transformaciones
- Genera nuevas columnas:
  - **Cambio absoluto de precio (`Price_Change`)**: Diferencia entre `High` y `Low`.
  - **Volatilidad intradía (`Intraday_Volatility`)**: Relación entre `(High - Low) / Open`.
- Escala columnas numéricas como `Price`, `Open`, `High`, y `Low` si es necesario.

### 4. Detección de Anomalías
- Identifica valores atípicos en las columnas `Price` y `Change %` utilizando un umbral de desviación estándar configurable.
- Opciones de tratamiento:
  - **Eliminar anomalías** (predeterminado).
  - **Imputar anomalías** mediante interpolación.

### 5. Generación de Indicadores Técnicos
Agrega indicadores financieros comunes al DataFrame:
- **Media Móvil Simple (SMA)**:
  - Ventanas de 5, 10 y 20 días.
- **Índice de Fuerza Relativa (RSI)**:
  - Calcula niveles de sobrecompra o sobreventa.
- **Bandas de Bollinger**:
  - Basadas en SMA de 20 días y desviación estándar.
- **MACD (Media Móvil de Convergencia/Divergencia)**:
  - Incluye la línea de señal.

### 6. Exportación
- Guarda el DataFrame procesado en `data/processed/` con un nombre basado en un timestamp (`USD_EUR_cleaned_<timestamp>.csv`).

---

## Requerimientos

- **Python >= 3.10**.
- Librerías:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - Otras mencionadas en `requirements.txt`.

Instala las dependencias con:
```bash
pip install -r requirements.txt
