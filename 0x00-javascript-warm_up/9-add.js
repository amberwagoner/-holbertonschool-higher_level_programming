#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const [arg1, arg2] = process.argv.slice(2);
const parsedInt1 = parseInt(arg1);
const parsedInt2 = parseInt(arg2);

if (isNaN(parsedInt1) || isNaN(parsedInt2)) {
  console.log('NaN');
} else {
  const result = add(parsedInt1, parsedInt2);
  console.log(result);
}
