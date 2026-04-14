from src.simulation import generate_synthetic_climate_data
from src.preprocess import clean_climate_data
from src.anomaly_detection import detect_anomalies
from src.forecast import forecast_temperature


def test_pipeline_smoke():
    raw = generate_synthetic_climate_data()
    clean = clean_climate_data(raw)
    anomalies = detect_anomalies(clean)
    forecast = forecast_temperature(clean, periods=6)

    assert not clean.empty
    assert "temp_rolling_12" in clean.columns
    assert forecast.shape[0] == 6
    assert anomalies is not None
