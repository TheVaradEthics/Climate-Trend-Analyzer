import { useEffect, useMemo, useState } from 'react';
import {
  AreaChart,
  Area,
  CartesianGrid,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  Legend,
} from 'recharts';
import {
  Thermometer,
  CloudRain,
  Waves,
  Leaf,
  CalendarRange,
  AlertTriangle,
  Upload,
} from 'lucide-react';
import StatCard from './components/StatCard';
import SectionTitle from './components/SectionTitle';

const graphCards = [
  { title: 'Temperature Trend', file: '/graphs/temperature_trend.png' },
  { title: 'Rainfall Trend', file: '/graphs/rainfall_trend.png' },
  { title: 'Yearly Regional Temperature Comparison', file: '/graphs/yearly_region_temperature_comparison.png' },
  { title: 'Temperature Anomalies', file: '/graphs/temperature_anomalies.png' },
  { title: 'Temperature Forecast', file: '/graphs/temperature_forecast.png' },
];

function formatNumber(value, digits = 2) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '—';
  return Number(value).toFixed(digits);
}

export default function App() {
  const [report, setReport] = useState(null);
  const [error, setError] = useState('');
  const [loadedFromLocal, setLoadedFromLocal] = useState(false);

  useEffect(() => {
    fetch('/data/summary_report.json')
      .then((res) => {
        if (!res.ok) throw new Error('Could not load bundled report.');
        return res.json();
      })
      .then((data) => {
        setReport(data);
        setError('');
      })
      .catch((err) => setError(err.message));
  }, []);

  const handleUpload = async (event) => {
    const file = event.target.files?.[0];
    if (!file) return;
    try {
      const text = await file.text();
      const data = JSON.parse(text);
      setReport(data);
      setLoadedFromLocal(true);
      setError('');
    } catch {
      setError('Invalid JSON file. Upload the backend summary_report.json file.');
    }
  };

  const summary = report?.summary ?? {};
  const trend = report?.trend_metrics?.overall ?? {};
  const yearly = report?.yearly_temperature_summary ?? [];
  const forecast = report?.forecast_preview ?? [];

  const trendCards = useMemo(() => {
    const tempPerYear = trend.temperature_slope_per_month ? trend.temperature_slope_per_month * 12 : null;
    const rainPerYear = trend.rainfall_slope_per_month ? trend.rainfall_slope_per_month * 12 : null;
    const co2PerYear = trend.co2_slope_per_month ? trend.co2_slope_per_month * 12 : null;
    const seaPerYear = trend.sea_level_slope_per_month ? trend.sea_level_slope_per_month * 12 : null;

    return [
      {
        icon: Thermometer,
        label: 'Temperature Rise / Year',
        value: tempPerYear !== null ? `${formatNumber(tempPerYear)} °C` : '—',
        subtext: 'Estimated from overall monthly slope',
      },
      {
        icon: CloudRain,
        label: 'Rainfall Change / Year',
        value: rainPerYear !== null ? `${formatNumber(rainPerYear)} mm` : '—',
        subtext: 'Negative values suggest declining rainfall',
      },
      {
        icon: Leaf,
        label: 'CO₂ Growth / Year',
        value: co2PerYear !== null ? `${formatNumber(co2PerYear)} ppm` : '—',
        subtext: 'Rising atmospheric concentration',
      },
      {
        icon: Waves,
        label: 'Sea Level Rise / Year',
        value: seaPerYear !== null ? `${formatNumber(seaPerYear)} mm` : '—',
        subtext: 'Long-term gradual increase',
      },
    ];
  }, [trend]);

  return (
    <div className="app-shell">
      <header className="hero card">
        <div>
          <span className="badge">Climate Analytics Dashboard</span>
          <h1>Climate Trend Analyzer Frontend</h1>
          <p>
            A polished frontend that visualizes the backend-generated climate report, trend metrics,
            forecast preview, and analysis graphs in one recruiter-friendly dashboard.
          </p>
        </div>
        <label className="upload-btn">
          <Upload size={18} />
          <span>Load summary_report.json</span>
          <input type="file" accept="application/json" onChange={handleUpload} />
        </label>
      </header>

      {error ? <div className="alert error">{error}</div> : null}
      {loadedFromLocal ? (
        <div className="alert success">Loaded data from your uploaded backend report file.</div>
      ) : null}

      <section className="grid stats-grid">
        <StatCard icon={CalendarRange} label="Date Range" value={summary?.date_range ? `${summary.date_range.start} → ${summary.date_range.end}` : '—'} subtext={`${summary?.rows ?? 0} records analysed`} />
        <StatCard icon={Thermometer} label="Average Temperature" value={summary?.temperature_summary ? `${formatNumber(summary.temperature_summary.mean)} °C` : '—'} subtext={`Max ${formatNumber(summary?.temperature_summary?.max)} °C`} />
        <StatCard icon={CloudRain} label="Average Rainfall" value={summary?.rainfall_summary ? `${formatNumber(summary.rainfall_summary.mean)} mm` : '—'} subtext={`Max ${formatNumber(summary?.rainfall_summary?.max)} mm`} />
        <StatCard icon={AlertTriangle} label="Anomalies Detected" value={report?.anomaly_count ?? 0} subtext={`${summary?.regions?.length ?? 0} regions covered`} />
      </section>

      <section className="panel-grid">
        <div className="card panel tall">
          <SectionTitle title="Yearly Temperature Pattern" subtitle="Average annual temperature from the backend summary report" />
          <div className="chart-wrap">
            <ResponsiveContainer width="100%" height={320}>
              <AreaChart data={yearly}>
                <defs>
                  <linearGradient id="tempFill" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="currentColor" stopOpacity={0.35} />
                    <stop offset="95%" stopColor="currentColor" stopOpacity={0.02} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis />
                <Tooltip />
                <Area type="monotone" dataKey="temperature_c" strokeWidth={3} fill="url(#tempFill)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="card panel tall">
          <SectionTitle title="Forecast Preview" subtitle="Projected average temperature values from the backend forecast module" />
          <div className="chart-wrap">
            <ResponsiveContainer width="100%" height={320}>
              <LineChart data={forecast}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" tickFormatter={(v) => v.slice(0, 7)} />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="forecast_temperature_c" strokeWidth={3} dot={false} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </section>

      <section>
        <SectionTitle title="Trend Snapshot" subtitle="Overall change per year estimated from the backend trend slopes" />
        <div className="grid stats-grid">
          {trendCards.map((item) => (
            <StatCard key={item.label} {...item} />
          ))}
        </div>
      </section>

      <section className="panel-grid two-thirds">
        <div className="card panel">
          <SectionTitle title="Regional Trend Metrics" subtitle="Directly mapped from the backend summary file" />
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Region</th>
                  <th>Temp / Month</th>
                  <th>Rain / Month</th>
                  <th>CO₂ / Month</th>
                  <th>Sea Level / Month</th>
                </tr>
              </thead>
              <tbody>
                {Object.entries(report?.trend_metrics?.by_region ?? {}).map(([region, values]) => (
                  <tr key={region}>
                    <td>{region}</td>
                    <td>{formatNumber(values.temperature_slope_per_month, 4)}</td>
                    <td>{formatNumber(values.rainfall_slope_per_month, 4)}</td>
                    <td>{formatNumber(values.co2_slope_per_month, 4)}</td>
                    <td>{formatNumber(values.sea_level_slope_per_month, 4)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <div className="card panel">
          <SectionTitle title="Climate Summary Means" subtitle="Average values from the cleaned dataset" />
          <div className="chart-wrap">
            <ResponsiveContainer width="100%" height={320}>
              <BarChart
                data={[
                  { name: 'Temp °C', value: summary?.temperature_summary?.mean ?? 0 },
                  { name: 'Rain mm', value: summary?.rainfall_summary?.mean ?? 0 },
                  { name: 'CO₂ ppm', value: summary?.co2_summary?.mean ?? 0 },
                  { name: 'Sea mm', value: summary?.sea_level_summary?.mean ?? 0 },
                ]}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="value" radius={[10, 10, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </section>

      <section>
        <SectionTitle title="Backend Generated Graphs" subtitle="These PNG charts are bundled from the backend outputs folder for direct demonstration." />
        <div className="gallery-grid">
          {graphCards.map((graph) => (
            <div key={graph.title} className="card gallery-card">
              <img src={graph.file} alt={graph.title} />
              <div className="gallery-meta">
                <h3>{graph.title}</h3>
                <p>Included from backend outputs for a complete portfolio demo.</p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
