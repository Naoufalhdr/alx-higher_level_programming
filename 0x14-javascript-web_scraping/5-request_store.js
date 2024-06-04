#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Extract command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a Get request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Status code:', response.statusCode);
    return;
  }

  // Write the response body to the file
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
