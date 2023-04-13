#!/usr/bin/node
// Task 2
const request = require('request');
if (process.argv.length < 3) {
  console.error('URL needed');
} else {
  const url = process.argv[2];
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(`Error occurred while making the GET request: ${error}`);
      return;
    }
    console.log('code: ' + response.statusCode);
  });
}
