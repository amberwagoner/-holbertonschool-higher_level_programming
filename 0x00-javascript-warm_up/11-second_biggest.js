#!/usr/bin/node
const args = process.argv.slice(2);
const intArgs = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));
const sortedIntArgs = intArgs.sort((a, b) => b - a);

if (sortedIntArgs.length === 0) {
  console.log(0);
} else if (sortedIntArgs.length === 1) {
  console.log(0);
} else {
  console.log(sortedIntArgs[1]);
}
