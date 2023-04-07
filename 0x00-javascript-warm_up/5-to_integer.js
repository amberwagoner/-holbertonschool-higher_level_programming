#!/usr/bin/node
const [arg1] = process.argv.slice(2);
const parsedInt = parseInt(arg1);

if (isNaN(parsedInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedInt}`);
}
