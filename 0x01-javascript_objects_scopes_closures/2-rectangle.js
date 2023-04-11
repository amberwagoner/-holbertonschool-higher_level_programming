#!/usr/bin/node
// Task 2
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Return empty object for invalid input
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
