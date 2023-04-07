#!/usr/bin/node
const [arg1] = process.argv.slice(2);

if (!arg1) {
  console.log('No argument');
} else {
  console.log(arg1);
}
