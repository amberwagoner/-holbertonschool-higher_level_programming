#!/usr/bin/node
// Task 1
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('arg error');
} else {
  const filePath = process.argv[2];
  const contentToWrite = process.argv[3];

  fs.writeFile(filePath, contentToWrite, 'utf-8', (error) => {
    if (error) {
      console.error(`Error occurred while writing to the file: ${error}`);
    }
  });
}
