#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data1) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }

  fs.readFile(process.argv[3], 'utf8', (err, data2) => {
    if (err) {
      console.error('Error reading file:', err);
      return;
    }

    const result = data1 + data2;

    fs.writeFile(process.argv[4], result, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file ' + process.argv[4] + ' :', err);
      }
    });
  });
});
