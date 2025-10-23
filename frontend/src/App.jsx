import React, { useEffect, useState } from "react";

const API_BASE = "https://foodture-dashboard.onrender.com";

export default function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [start, setStart] = useState("2025-10-01");
  const [end, setEnd] = useState("2025-10-31");

  useEffect(() => {
    (async () => {
      try {
        setLoading(true);
        setError("");
        const res = await fetch(`${API_BASE}/api/overview?start=${start}&end=${end}`);
        const json = await res.json();
        setData(json);
      } catch (e) {
        setError(String(e));
      } finally {
        setLoading(false);
      }
    })();
  }, [start, end]);

  return (
    <div style={{ maxWidth: "800px", margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>Foodture Dashboard</h1>
      <div>
        <input type="date" value={start} onChange={(e) => setStart(e.target.value)} />
        <input type="date" value={end} onChange={(e) => setEnd(e.target.value)} />
      </div>
      {loading && <p>Loading…</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {data && data.totals && (
        <pre>{JSON.stringify(data.totals, null, 2)}</pre>
      )}
    </div>
  );
}
