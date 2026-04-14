import pandas as pd


def generate_basic_summary(df: pd.DataFrame) -> dict:
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "date_range": {
            "start": str(df["date"].min().date()),
            "end": str(df["date"].max().date()),
        },
        "regions": sorted(df["region"].unique().tolist()),
        "temperature_summary": df["temperature_c"].describe().round(3).to_dict(),
        "rainfall_summary": df["rainfall_mm"].describe().round(3).to_dict(),
        "co2_summary": df["co2_ppm"].describe().round(3).to_dict(),
        "sea_level_summary": df["sea_level_mm"].describe().round(3).to_dict(),
        "missing_values_after_cleaning": df.isna().sum().to_dict(),
    }
