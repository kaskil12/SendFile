const express = require('express');



const app = express();
const port = 3000;

app.post('/', (req , res ) => {
  res.send('Express + TypeScript Server');
});

app.listen(port, () => {
  console.log(`⚡️[server]: Server is running at http://localhost:${port}`);
});