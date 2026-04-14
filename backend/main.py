from pathlib import Path

from src.config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    OUTPUT_DIR,
    REPORT_JSON_PATH,
    ANOMALIES_CSV_PATH,
)
from src.data_loader import load_climate_data
from src.preprocess import clean_climate_data
from src.eda import generate_basic_summary
from src.trend_analysis import compute_trend_metrics
from src.anomaly_detection import detect_anomalies
from src.forecast import forecast_temperature
from src.visualize import create_all_visuals
from src.reporting import build_report
from src.simulation import generate_synthetic_climate_data


def ensure_input_data() -> None:
    if not RAW_DATA_PATH.exists():
        RAW_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        df = generate_synthetic_climate_data()
        df.to_csv(RAW_DATA_PATH, index=False)
        print(f"[INFO] Input dataset not found. Generated sample data at {RAW_DATA_PATH}")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ensure_input_data()

    raw_df = load_climate_data(RAW_DATA_PATH)
    clean_df = clean_climate_data(raw_df)
    clean_df.to_csv(PROCESSED_DATA_PATH, index=False)

    summary = generate_basic_summary(clean_df)
    trend_metrics = compute_trend_metrics(clean_df)

    anomalies_df = detect_anomalies(clean_df)
    anomalies_df.to_csv(ANOMALIES_CSV_PATH, index=False)

    forecast_df = forecast_temperature(clean_df, periods=24)
    create_all_visuals(clean_df, anomalies_df, forecast_df)

    report = build_report(
        summary=summary,
        trend_metrics=trend_metrics,
        anomalies_df=anomalies_df,
        forecast_df=forecast_df,
        processed_df=clean_df,
    )

    REPORT_JSON_PATH.write_text(report, encoding="utf-8")

    print("[SUCCESS] Climate Trend Analyzer pipeline completed.")
    print(f"[OUTPUT] Processed data: {PROCESSED_DATA_PATH}")
    print(f"[OUTPUT] Anomalies table: {ANOMALIES_CSV_PATH}")
    print(f"[OUTPUT] Report JSON: {REPORT_JSON_PATH}")
    print("[OUTPUT] Graphs saved in outputs/graphs/")


if __name__ == "__main__":
    main()
