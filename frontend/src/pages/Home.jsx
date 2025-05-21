import React, { useState } from 'react';
import '../App.css'
export default function Home() {
    const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const runSpeedTest = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:5000/web');      
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error('Error fetching speed test results:', error);
    } finally {
      setLoading(false);
    }
  };
    return (

        <div className="home">
            
            <h1>Welcome to Speed Test!</h1>
            <button className="start-button" onClick={runSpeedTest} disabled={loading}>
            {loading ? 'Running...' : 'Run Speed Test'}
            </button>
            {results && (
            <div>
                <p>Download Speed: {results.download} MB/s</p>
                <p>Upload Speed: {results.upload} MB/s</p>
                <p>Packet Loss: {results.packet_loss}%</p>
                <p>Average Ping: {results.avg_ping} ms</p>
            </div>
            )}
        </div>
    )
}