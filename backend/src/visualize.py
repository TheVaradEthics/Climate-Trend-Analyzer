from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

from src.config import GRAPH_DIR


def _save_plot(filename: str) -> None:
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / filename, dpi=150, bbox_inches="tight")
    plt.close()


def create_temperature_trend_plot(df: pd.DataFrame) -> None:
    overall = df.groupby("date", as_index=False)["temperature_c"].mean()

    plt.figure(figsize=(12, 5))
    plt.plot(overall["date"], overall["temperature_c"])
    plt.title("Average Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, alpha=0.3)
    _save_plot("temperature_trend.png")


def create_rainfall_trend_plot(df: pd.DataFrame) -> None:
    overall = df.groupby("date", as_index=False)["rainfall_mm"].mean()

    plt.figure(figsize=(12, 5))
    plt.plot(overall["date"], overall["rainfall_mm"])
    plt.title("Average Rainfall Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.grid(True, alpha=0.3)
    _save_plot("rainfall_trend.png")


def create_region_comparison_plot(df: pd.DataFrame) -> None:
    yearly = df.groupby(["year", "region"], as_index=False)["temperature_c"].mean()

    plt.figure(figsize=(12, 6))
    for region, region_df in yearly.groupby("region"):
        plt.plot(region_df["year"], region_df["temperature_c"], label=region)
    plt.title("Yearly Average Temperature by Region")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    _save_plot("yearly_region_temperature_comparison.png")


def create_anomaly_plot(df: pd.DataFrame, anomalies_df: pd.DataFrame) -> None:
    overall = df.groupby("date", as_index=False)["temperature_c"].mean()

    plt.figure(figsize=(12, 5))
    plt.plot(overall["date"], overall["temperature_c"], label="Average Temperature")

    if not anomalies_df.empty:
        anomaly_points = anomalies_df.groupby("date", as_index=False)["temperature_c"].mean()
        plt.scatter(anomaly_points["date"], anomaly_points["temperature_c"], label="Detected Anomalies")

    plt.title("Temperature Anomaly Detection")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    _save_plot("temperature_anomalies.png")


def create_forecast_plot(df: pd.DataFrame, forecast_df: pd.DataFrame) -> None:
    historical = df.groupby("date", as_index=False)["temperature_c"].mean()

    plt.figure(figsize=(12, 5))
    plt.plot(historical["date"], historical["temperature_c"], label="Historical Temperature")
    plt.plot(forecast_df["date"], forecast_df["forecast_temperature_c"], label="Forecast Temperature")
    plt.title("Temperature Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    _save_plot("temperature_forecast.png")


def create_all_visuals(df: pd.DataFrame, anomalies_df: pd.DataFrame, forecast_df: pd.DataFrame) -> None:
    create_temperature_trend_plot(df)
    create_rainfall_trend_plot(df)
    create_region_comparison_plot(df)
    create_anomaly_plot(df, anomalies_df)
    create_forecast_plot(df, forecast_df)
