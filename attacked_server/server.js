const express = require('express');
const morgan = require('morgan');
const app = express();

app.use(morgan('combined'));

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Attacked server is running on port ${PORT}`);
});
