# Climate Trend Analyzer Frontend

A professional React + Vite dashboard that matches the Climate Trend Analyzer backend. It reads the backend-generated `summary_report.json` and displays climate KPIs, yearly trends, forecast preview, regional metrics, and bundled graph outputs.

## Features
- Recruiter-friendly climate dashboard UI
- Reads backend `summary_report.json`
- Includes bundled sample backend graphs for instant demo
- Supports loading a fresh backend report using the upload button
- Fully responsive layout

## Tech Stack
- React
- Vite
- Recharts
- Lucide React
- Custom CSS

## Project Structure
```text
Climate-Trend-Analyzer-Frontend/
├── public/
│   ├── data/
│   │   └── summary_report.json
│   └── graphs/
│       ├── temperature_trend.png
│       ├── rainfall_trend.png
│       ├── yearly_region_temperature_comparison.png
│       ├── temperature_anomalies.png
│       └── temperature_forecast.png
├── src/
│   ├── components/
│   │   ├── SectionTitle.jsx
│   │   └── StatCard.jsx
│   ├── App.jsx
│   ├── main.jsx
│   └── styles.css
├── index.html
├── package.json
├── vite.config.js
├── .gitignore
└── README.md
```

## Installation
```bash
npm install
npm run dev
```

## Build for production
```bash
npm run build
npm run preview
```

## How it matches the backend
This frontend is designed around the backend zip that generates:
- `outputs/reports/summary_report.json`
- `outputs/graphs/*.png`

The frontend already includes one generated summary report and graph set from the backend for demo use.

## Using your own backend output
1. Run the backend pipeline.
2. Open the frontend.
3. Use the **Load summary_report.json** button and select the newly generated backend report file.
4. For updated images, replace the files inside `public/graphs/` with the latest backend graph PNGs.

## Ideal demo flow
1. Show backend outputs folder.
2. Open frontend dashboard.
3. Upload `summary_report.json`.
4. Explain cards, trends, forecast, and anomalies.

## GitHub repository name
`climate-trend-analyzer-frontend`
