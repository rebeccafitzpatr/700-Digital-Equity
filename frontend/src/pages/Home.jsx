import React, { useState, useEffect } from 'react';
import '../App.css'
import { measureDownloadSpeed, measureLatency, measureUploadSpeed } from '../ClientSpeedTest.js';

export default function Home() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const username = localStorage.getItem('username');

  useEffect(() => {
    const savedResults = localStorage.getItem('speedtestResults');
    if (savedResults) {
      setResults(JSON.parse(savedResults));
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('username');
    localStorage.removeItem('speedtestResults');
    setResults(null);
    window.location.reload(); // or use navigate('/') if using react-router
  };

  const runSpeedTest = async () => {
    setLoading(true);
    // Check for logged-in user (adjust this logic as needed)
    navigator.geolocation.getCurrentPosition(
      async (position) => {
        try {
          const { latitude, longitude } = position.coords;
          // Send latitude and longitude to backend with the speed test result
          const latency = await measureLatency();
          const downloadSpeed = await measureDownloadSpeed();
          const uploadSpeed = await measureUploadSpeed();

          const result = {
            username: username || 'guest',
            download: downloadSpeed,
            avg_ping: latency,
            upload: uploadSpeed,
            latitude,
            longitude
          };

          await fetch('/api/speedtest', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(result)
        });


          setResults(result)
          setLoading(false);
        } catch (error) {
          console.error('Error fetching speed test results:', error);
        } finally {
          setLoading(false);
        }
      },
      (error) => {
        console.error('Geolocation error:', error);
        setLoading(false);
      }
    );
  };
    return (

        <div className="home">
            
            <h1>
              {username ? `Welcome, ${username}` : 'Welcome to Speed Test!'}
            </h1>
              
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

            {username && (
              <button onClick={handleLogout} style={{ marginBottom: '1rem' }}>
                Logout
              </button>
            )}  
        </div>
    )
}