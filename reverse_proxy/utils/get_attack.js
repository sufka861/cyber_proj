const { RateLimiterRedis } = require('rate-limiter-flexible');
const { createClient } = require('redis');

// Read Redis host and port from environment variables
const redisHost = process.env.REDIS_HOST || 'redis'; // Default to Docker service name 'redis'
const redisPort = process.env.REDIS_PORT || 6380; // Custom Redis port

// Create a Redis client
const redisClient = createClient({
  url: `redis://${redisHost}:${redisPort}`,
  legacyMode: true // Enable legacy mode for older Redis commands
});
redisClient.connect().catch(console.error);

// Configure rate limiter
const rateLimiter = new RateLimiterRedis({
  storeClient: redisClient,
  keyPrefix: 'rateLimiter',
  points: 10, // 10 requests
  duration: 10, // per 10 seconds by IP
  blockDuration: 60, // block for 1 minute if more than points consumed
});

// Middleware to check rate limit and block IPs
const rateLimiterMiddleware = (req, res, next) => {
  rateLimiter.consume(req.ip)
    .then(() => {
      next();
    })
    .catch(() => {
      res.status(429).send('Too many requests - try again in a minute');
    });
};

module.exports = { rateLimiterMiddleware };
