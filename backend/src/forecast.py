import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def forecast_temperature(df: pd.DataFrame, periods: int = 24) -> pd.DataFrame:
    overall = (
        df.groupby("date", as_index=False)["temperature_c"]
        .mean()
        .sort_values("date")
        .reset_index(drop=True)
    )

    overall["time_index"] = np.arange(len(overall))
    model = LinearRegression()
    X = overall[["time_index"]]
    y = overall["temperature_c"]
    model.fit(X, y)

    future_index = np.arange(len(overall), len(overall) + periods)
    preds = model.predict(future_index.reshape(-1, 1))

    last_date = overall["date"].max()
    future_dates = pd.date_range(last_date + pd.offsets.MonthBegin(1), periods=periods, freq="MS")

    forecast_df = pd.DataFrame(
        {
            "date": future_dates,
            "forecast_temperature_c": preds.round(3),
        }
    )
    return forecast_df
