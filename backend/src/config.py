from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "climate_data.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "climate_data_cleaned.csv"

OUTPUT_DIR = BASE_DIR / "outputs"
GRAPH_DIR = OUTPUT_DIR / "graphs"
REPORT_DIR = OUTPUT_DIR / "reports"
TABLE_DIR = OUTPUT_DIR / "tables"

REPORT_JSON_PATH = REPORT_DIR / "summary_report.json"
ANOMALIES_CSV_PATH = TABLE_DIR / "temperature_anomalies.csv"

for path in [GRAPH_DIR, REPORT_DIR, TABLE_DIR, PROCESSED_DATA_PATH.parent, RAW_DATA_PATH.parent]:
    path.mkdir(parents=True, exist_ok=True)
