#!/usr/bin/node
const [arg1] = process.argv.slice(2);
const parsedInt = parseInt(arg1);

if (isNaN(parsedInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsedInt; i++) {
    console.log('X'.repeat(parsedInt));
  }
}
