#!/usr/bin/node
// Task 7: Occurences
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let i = 0; i < list.lenth; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  return count;
};
