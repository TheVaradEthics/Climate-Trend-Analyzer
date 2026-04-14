from src.simulation import generate_synthetic_climate_data
from src.config import RAW_DATA_PATH

if __name__ == "__main__":
    df = generate_synthetic_climate_data()
    df.to_csv(RAW_DATA_PATH, index=False)
    print(f"Sample climate dataset saved to: {RAW_DATA_PATH}")
    print(df.head())
