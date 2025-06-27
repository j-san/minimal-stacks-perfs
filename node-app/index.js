// import express from 'express';

// const app = express();
// const PORT = process.env.PORT || 3000;

// // Basic health check route
// app.get('/', (req, res) => {
//   res.send('Hello, world!');
// });

// app.listen(PORT, () => {
//   console.log(`Server running on port ${PORT}`);
// });

import http from 'http';

http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello, world!');
}).listen(3000);