const express = require('express');
const morgan = require('morgan');
const app = express();

app.use(morgan('combined'));

// Set the timeout for the server to a high value (e.g., 10 minutes)
const serverTimeout = 10 * 60 * 1000; // 10 minutes in milliseconds
app.use((req, res, next) => {
  req.setTimeout(serverTimeout);
  res.setTimeout(serverTimeout);
  next();
});

// Middleware to log connection attempts
app.use((req, res, next) => {
  console.log(`Received request: ${req.method} ${req.url}`);
  
  // Log request headers
  for (let header in req.headers) {
    console.log(`Header: ${header} = ${req.headers[header]}`);
  }

  req.on('data', chunk => {
    console.log(`Received data: ${chunk}`);
  });

  req.on('end', () => {
    console.log('Request ended');
  });

  next();
});

// Debugging middleware to log raw incoming requests
app.use((req, res, next) => {
  console.log('Raw request:', req.rawHeaders);
  next();
});

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

const PORT = 3000;
const server = app.listen(PORT, () => {
  console.log(`Attacked server is running on port ${PORT}`);
});

// Set the timeout for the server
server.setTimeout(serverTimeout);

// Add a connection event to log all connections
server.on('connection', (socket) => {
  console.log('New connection from:', socket.remoteAddress);
  socket.on('data', (chunk) => {
    console.log(`Received chunk: ${chunk}`);
  });
});
