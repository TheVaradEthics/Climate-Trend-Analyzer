import numpy as np
import pandas as pd


def generate_synthetic_climate_data(
    start="2010-01-01",
    end="2024-12-01",
    regions=None,
    seed=42,
) -> pd.DataFrame:
    if regions is None:
        regions = ["North", "South", "East", "West"]

    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start, end=end, freq="MS")
    rows = []

    for region_index, region in enumerate(regions):
        base_temp = 22 + (region_index * 1.5)
        base_rain = 80 + (region_index * 8)
        base_co2 = 385
        base_sea = 0 + region_index * 2

        for i, date in enumerate(dates):
            month = date.month

            seasonal_temp = 8 * np.sin((2 * np.pi * month) / 12)
            warming_trend = 0.03 * i
            temp_noise = rng.normal(0, 1.4)

            seasonal_rain = 45 * max(np.sin((2 * np.pi * (month - 2)) / 12), -0.3)
            rain_noise = rng.normal(0, 10)
            rainfall = max(0, base_rain + seasonal_rain + rain_noise)

            co2_ppm = base_co2 + 0.12 * i + rng.normal(0, 0.5)
            sea_level_mm = base_sea + 0.25 * i + rng.normal(0, 1.0)

            temperature_c = base_temp + seasonal_temp + warming_trend + temp_noise

            # Simulate rare anomalies
            if rng.random() < 0.015:
                temperature_c += rng.choice([5.5, -6.0])
            if rng.random() < 0.015:
                rainfall *= rng.choice([0.2, 2.2])

            rows.append(
                {
                    "date": date.strftime("%Y-%m-%d"),
                    "region": region,
                    "temperature_c": round(float(temperature_c), 2),
                    "rainfall_mm": round(float(rainfall), 2),
                    "co2_ppm": round(float(co2_ppm), 2),
                    "sea_level_mm": round(float(sea_level_mm), 2),
                }
            )

    return pd.DataFrame(rows)
