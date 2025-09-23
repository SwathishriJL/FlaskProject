/* Base Styles */
body {
  margin: 0;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: var(--bg);
  color: var(--text);
  transition: all 0.3s ease-in-out;
}

.app {
  padding: 20px;
}

/* Theme Variables */
:root {
  --bg: #f9f9f9;
  --text: #222;
  --card: #fff;
  --primary: #4cafef;
  --error: #e74c3c;
}

.dark {
  --bg: #181818;
  --text: #f1f1f1;
  --card: #242424;
  --primary: #3498db;
  --error: #ff6b6b;
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--card);
  padding: 15px 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.theme-toggle {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.3rem;
  color: var(--text);
}

/* Button */
.analyze-btn {
  padding: 12px 25px;
  margin: 20px 0;
  background-color: var(--primary);
  border: none;
  color: white;
  cursor: pointer;
  border-radius: 6px;
  font-size: 1rem;
  transition: background 0.3s;
}

.analyze-btn:disabled {
  background-color: #888;
  cursor: not-allowed;
}

.analyze-btn:hover:not(:disabled) {
  background-color: #2c8bd6;
}

/* Results Section */
.results {
  margin-top: 20px;
}

.error {
  color: var(--error);
  font-weight: bold;
  margin: 10px 0;
}

.folder-section {
  background: var(--card);
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.08);
}

.folder-section h3 {
  margin-top: 0;
  color: var(--primary);
}

/* Styled Table */
.styled-table {
  border-collapse: collapse;
  margin: 15px 0;
  font-size: 0.95em;
  min-width: 500px;
  border: 1px solid #ddd;
  width: 100%;
}

.styled-table th,
.styled-table td {
  border: 1px solid #ddd;
  padding: 10px;
}

.styled-table tr:nth-child(even) {
  background-color: rgba(0, 0, 0, 0.03);
}

.styled-table th {
  background-color: var(--primary);
  color: white;
  text-align: left;
}
