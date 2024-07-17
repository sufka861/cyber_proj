const rateLimit = require('express-rate-limit');

// Limit the number of open connections from a single IP
const connectionLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 10, // limit each IP to 10 connections per windowMs
  handler: (req, res) => {
    res.status(429).send('Too many connections - try again later');
  }
});

// Middleware to set a timeout for header reception
const headerTimeoutMiddleware = (req, res, next) => {
  req.setTimeout(5000, () => { // 5 seconds
    res.status(408).send('Request timeout - headers not received in time');
  });
  next();
};

// Middleware to set a connection timeout
const connectionTimeoutMiddleware = (req, res, next) => {
  res.setTimeout(30000, () => { // 30 seconds
    res.status(408).send('Request timeout - connection idle too long');
  });
  next();
};

module.exports = {
  connectionLimiter,
  headerTimeoutMiddleware,
  connectionTimeoutMiddleware
};
