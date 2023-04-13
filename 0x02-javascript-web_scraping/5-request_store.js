#!/usr/bin/node
// Task 5
const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('URL needed');
} else {
  const url = process.argv[2];
  const filePath = process.argv[3];

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(`Error occurred while making the GET request: ${error}`);
      return;
    }

    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error(`Error occurred while writing to the file: ${error}`);
      }
    });
  });
}
