#!/usr/bin/node
const [arg1, arg2] = process.argv.slice(2);

if (!arg1 || !arg2) {
    console.log("Please provide two arguments");
}
else {
    console.log(`${arg1} is ${arg2}`);
}
