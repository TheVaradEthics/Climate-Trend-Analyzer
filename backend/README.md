# Climate Trend Analyzer Backend

A backend-focused Python project for climate trend analysis using public-style simulated data.

## Features
- Synthetic climate dataset generation
- Data cleaning and preprocessing
- Exploratory summaries
- Trend analysis with yearly and monthly views
- Anomaly detection using z-score and rolling deviation
- Forecasting using linear regression and optional ARIMA
- Saves graphs, tables, and a JSON summary report

## Project Structure
- `main.py` - runs the full pipeline
- `generate_sample_data.py` - creates sample climate dataset
- `src/config.py` - paths and project settings
- `src/data_loader.py` - load dataset
- `src/preprocess.py` - cleaning and feature engineering
- `src/eda.py` - descriptive analysis
- `src/trend_analysis.py` - long-term trend calculations
- `src/anomaly_detection.py` - anomaly detection logic
- `src/forecast.py` - future forecasting
- `src/visualize.py` - chart generation
- `src/reporting.py` - JSON/text report creation

## Quick Start

### 1. Create virtual environment
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate sample dataset
```bash
python generate_sample_data.py
```

### 4. Run full backend pipeline
```bash
python main.py
```

## Outputs
After running, you will get:
- processed dataset in `data/processed/`
- graphs in `outputs/graphs/`
- anomaly table in `outputs/tables/`
- summary report in `outputs/reports/`

## Input Dataset Format
CSV with columns:
- `date`
- `region`
- `temperature_c`
- `rainfall_mm`
- `co2_ppm`
- `sea_level_mm`

## Notes
This backend is designed to be beginner-friendly and portfolio-ready.
