import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def _slope_for_series(values: pd.Series) -> float:
    x = np.arange(len(values)).reshape(-1, 1)
    y = values.to_numpy()
    model = LinearRegression()
    model.fit(x, y)
    return float(model.coef_[0])


def compute_trend_metrics(df: pd.DataFrame) -> dict:
    metrics = {"by_region": {}, "overall": {}}

    overall_monthly = df.groupby("date", as_index=False).agg(
        temperature_c=("temperature_c", "mean"),
        rainfall_mm=("rainfall_mm", "mean"),
        co2_ppm=("co2_ppm", "mean"),
        sea_level_mm=("sea_level_mm", "mean"),
    )

    metrics["overall"] = {
        "temperature_slope_per_month": round(_slope_for_series(overall_monthly["temperature_c"]), 4),
        "rainfall_slope_per_month": round(_slope_for_series(overall_monthly["rainfall_mm"]), 4),
        "co2_slope_per_month": round(_slope_for_series(overall_monthly["co2_ppm"]), 4),
        "sea_level_slope_per_month": round(_slope_for_series(overall_monthly["sea_level_mm"]), 4),
    }

    for region, region_df in df.groupby("region"):
        monthly = region_df.groupby("date", as_index=False).agg(
            temperature_c=("temperature_c", "mean"),
            rainfall_mm=("rainfall_mm", "mean"),
            co2_ppm=("co2_ppm", "mean"),
            sea_level_mm=("sea_level_mm", "mean"),
        )
        metrics["by_region"][region] = {
            "temperature_slope_per_month": round(_slope_for_series(monthly["temperature_c"]), 4),
            "rainfall_slope_per_month": round(_slope_for_series(monthly["rainfall_mm"]), 4),
            "co2_slope_per_month": round(_slope_for_series(monthly["co2_ppm"]), 4),
            "sea_level_slope_per_month": round(_slope_for_series(monthly["sea_level_mm"]), 4),
        }

    return metrics
