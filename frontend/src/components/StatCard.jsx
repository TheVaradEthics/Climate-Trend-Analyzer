export default function StatCard({ icon: Icon, label, value, subtext }) {
  return (
    <div className="card stat-card">
      <div className="stat-top">
        <div>
          <p className="label">{label}</p>
          <h3>{value}</h3>
        </div>
        {Icon ? <Icon size={20} /> : null}
      </div>
      {subtext ? <p className="muted">{subtext}</p> : null}
    </div>
  );
}
