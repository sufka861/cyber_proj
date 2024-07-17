const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const { rateLimiterMiddleware } = require('./utils/get_attack');

const app = express();

app.use(rateLimiterMiddleware);

app.use('/', createProxyMiddleware({ target: 'http://attacked_server:3000', changeOrigin: true }));

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Reverse proxy is running on port ${PORT}`);
});
