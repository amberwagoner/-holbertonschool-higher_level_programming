#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const [arg1] = process.argv.slice(2);
const parsedInt = parseInt(arg1);

console.log(factorial(parsedInt));
