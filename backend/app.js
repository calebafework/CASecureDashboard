const express = require('express');
const cors = require('cors');

const { addLog, getLogs } = require('./services/LogStore');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// Health check route
app.get('/api/health', (req, res) => {
  res.json({
    status: 'OK',
    uptime: process.uptime(),
    message: 'All systems operational',
    timestamp: new Date(),
  });
});

// Logs route
app.get('/api/logs', (req, res) => {
    res.json(getLogs())
});

app.post('/api/push-log', (req, res) => {
    const { type, message, service } = req.body;
    if (!type || !message || !service) {
        return res.status(400).json({ error: 'Missing type or message' });
    }

    addLog({ type, message, service });
    res.status(201).json({ status: 'Log added' });
})

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
