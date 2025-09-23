import React, { useState } from "react";
import { FaSun, FaMoon } from "react-icons/fa";
import "./App.css";

function App() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [darkMode, setDarkMode] = useState(false);

  const analyzeData = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch("http://localhost:5000/analyze", {
        method: "POST",
      });

      if (response.ok) {
        const result = await response.json();
        setData(result);
      } else {
        const errText = await response.text();
        setError(errText);
      }
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  return (
    <div className={darkMode ? "app dark" : "app"}>
      <header className="header">
        <h2>🔍 API Analyzer</h2>
        <button
          className="theme-toggle"
          onClick={() => setDarkMode(!darkMode)}
        >
          {darkMode ? <FaSun /> : <FaMoon />}
        </button>
      </header>

      <button className="analyze-btn" onClick={analyzeData} disabled={loading}>
        {loading ? "Analyzing..." : "Start Analysis"}
      </button>

      <div className="results">
        {error && <p className="error">❌ Error: {error}</p>}

        {data &&
          Object.entries(data).map(([folder, result], idx) => (
            <div key={idx} className="folder-section">
              <h3>{folder}</h3>
              <div className="comparison">
                {result.comparison ? (
                  <div
                    dangerouslySetInnerHTML={{
                      __html: result.comparison.replace(
                        "<table",
                        '<table class="styled-table"'
                      ),
                    }}
                  />
                ) : (
                  <p>No comparison available</p>
                )}
              </div>
              <hr />
            </div>
          ))}
      </div>
    </div>
  );
}

export default App;
