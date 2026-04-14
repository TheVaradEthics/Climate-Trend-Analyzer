import json
import pandas as pd


def build_report(
    summary: dict,
    trend_metrics: dict,
    anomalies_df: pd.DataFrame,
    forecast_df: pd.DataFrame,
    processed_df: pd.DataFrame,
) -> str:
    yearly_temp = (
        processed_df.groupby("year", as_index=False)["temperature_c"]
        .mean()
        .round(3)
        .to_dict(orient="records")
    )

    season_temp = (
        processed_df.groupby("season", as_index=False)["temperature_c"]
        .mean()
        .round(3)
        .to_dict(orient="records")
    )

    report = {
        "project": "Climate Trend Analyzer Backend",
        "summary": summary,
        "trend_metrics": trend_metrics,
        "anomaly_count": int(anomalies_df.shape[0]),
        "forecast_preview": forecast_df.head(10).assign(date=forecast_df["date"].astype(str)).to_dict(orient="records"),
        "yearly_temperature_summary": yearly_temp,
        "seasonal_temperature_summary": season_temp,
        "insights": [
            "Temperature trend slope above zero suggests long-term warming in the dataset.",
            "Rainfall trend should be interpreted along with seasonality because rainfall is highly seasonal.",
            "Anomalies highlight unusual months that deserve additional investigation.",
            "CO2 and sea level variables usually move upward in the simulated climate-change scenario.",
        ],
    }

    return json.dumps(report, indent=2)
