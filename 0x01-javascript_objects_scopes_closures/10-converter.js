#!/usr/bin/node
// Task 10
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
