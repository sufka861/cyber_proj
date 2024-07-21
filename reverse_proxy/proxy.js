const express = require('express');
const fs = require('fs');
const https = require('https');
const { createProxyMiddleware } = require('http-proxy-middleware');
const { rateLimiterMiddleware } = require('./utils/get_attack');  
const {
  connectionLimiter,
  headerTimeoutMiddleware,
  connectionTimeoutMiddleware
} = require('./utils/slowloris_attack');


const app = express();

// Load SSL key and certificate
const sslOptions = {
  key: fs.readFileSync('./server.key'),
  cert: fs.readFileSync('./server.cert')
};

// GET flood defense
app.use(rateLimiterMiddleware);

// SLOWLORIS defense
app.use(connectionLimiter);
app.use(headerTimeoutMiddleware);
app.use(connectionTimeoutMiddleware);


app.use('/', createProxyMiddleware({
  target: 'http://attacked_server:3000',
  changeOrigin: true,
  secure: false // Set to false if you do not want to verify SSL Certs
}));

const PORT = 3001;
https.createServer(sslOptions, app).listen(3001, () => {
  console.log('Reverse proxy is running on HTTPS port 3001');
});
