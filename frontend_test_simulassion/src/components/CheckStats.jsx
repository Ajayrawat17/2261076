import { useState } from "react";
import { customRequest } from "../api";

const CheckStats = () => {
  const [code, setCode] = useState('');
  const [stats, setStats] = useState(null);

  const fetchStats = async () => {
    const res = await customRequest(`/shorturls/${code}/`, {}, 'GET');
    setStats(res);
  };

  return (
    <div>
      <input placeholder="Enter Code"
             onChange={(e) => setCode(e.target.value)} />
      <button onClick={fetchStats}>Get Info</button>

      {stats?.url && (
        <div>
          <p><strong>Original:</strong> {stats.url}</p>
          <p><strong>Clicks:</strong> {stats.total_clicks}</p>
        </div>
      )}
    </div>
  );
};

export default CheckStats;
