const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
// GET flood imports
const { rateLimiterMiddleware } = require('./utils/get_attack');  

// SLOWLORIS imports
const {
  connectionLimiter,
  headerTimeoutMiddleware,
  connectionTimeoutMiddleware
} = require('./utils/slowloris_attack');

const app = express();

// GET flood defense
app.use(rateLimiterMiddleware);

// SLOWLORIS defense
app.use(connectionLimiter);
app.use(headerTimeoutMiddleware);
app.use(connectionTimeoutMiddleware);

app.use('/', createProxyMiddleware({ target: 'http://attacked_server:3000', changeOrigin: true }));

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Reverse proxy is running on port ${PORT}`);
});
