import express from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

// Basic health check route
app.get('/', (req, res) => {
  res.send('Hello, world!');
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});