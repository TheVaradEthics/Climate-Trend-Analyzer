from pathlib import Path
import pandas as pd


def load_climate_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)
    required_columns = {"date", "region", "temperature_c", "rainfall_mm", "co2_ppm", "sea_level_mm"}
    missing = required_columns.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return df
