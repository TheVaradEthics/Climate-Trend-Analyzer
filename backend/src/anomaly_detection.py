import pandas as pd


def detect_anomalies(df: pd.DataFrame, z_threshold: float = 2.2) -> pd.DataFrame:
    anomaly_frames = []

    for region, region_df in df.groupby("region"):
        region_df = region_df.copy()
        mean = region_df["temperature_c"].mean()
        std = region_df["temperature_c"].std(ddof=0)

        if std == 0:
            region_df["temp_zscore"] = 0.0
        else:
            region_df["temp_zscore"] = (region_df["temperature_c"] - mean) / std

        region_df["is_temperature_anomaly"] = region_df["temp_zscore"].abs() >= z_threshold
        anomaly_frames.append(region_df)

    combined = pd.concat(anomaly_frames, ignore_index=True)
    anomalies = combined.loc[combined["is_temperature_anomaly"]].copy()
    anomalies = anomalies[
        [
            "date",
            "region",
            "temperature_c",
            "rainfall_mm",
            "co2_ppm",
            "sea_level_mm",
            "temp_zscore",
            "is_temperature_anomaly",
        ]
    ].sort_values(["region", "date"])
    return anomalies.reset_index(drop=True)
