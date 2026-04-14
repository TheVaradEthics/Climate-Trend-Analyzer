import pandas as pd


def clean_climate_data(df: pd.DataFrame) -> pd.DataFrame:
    clean_df = df.copy()

    clean_df["date"] = pd.to_datetime(clean_df["date"], errors="coerce")
    clean_df = clean_df.dropna(subset=["date", "region"])

    numeric_cols = ["temperature_c", "rainfall_mm", "co2_ppm", "sea_level_mm"]
    for col in numeric_cols:
        clean_df[col] = pd.to_numeric(clean_df[col], errors="coerce")
        clean_df[col] = clean_df.groupby("region")[col].transform(lambda s: s.fillna(s.median()))
        clean_df[col] = clean_df[col].fillna(clean_df[col].median())

    clean_df = clean_df.drop_duplicates()
    clean_df = clean_df.sort_values(["region", "date"]).reset_index(drop=True)

    clean_df["year"] = clean_df["date"].dt.year
    clean_df["month"] = clean_df["date"].dt.month
    clean_df["quarter"] = clean_df["date"].dt.quarter

    season_map = {
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Summer", 4: "Summer", 5: "Summer",
        6: "Monsoon", 7: "Monsoon", 8: "Monsoon", 9: "Monsoon",
        10: "Post-Monsoon", 11: "Post-Monsoon",
    }
    clean_df["season"] = clean_df["month"].map(season_map)

    clean_df["temp_rolling_12"] = (
        clean_df.groupby("region")["temperature_c"].transform(lambda s: s.rolling(12, min_periods=1).mean())
    )
    clean_df["rain_rolling_12"] = (
        clean_df.groupby("region")["rainfall_mm"].transform(lambda s: s.rolling(12, min_periods=1).mean())
    )

    return clean_df
