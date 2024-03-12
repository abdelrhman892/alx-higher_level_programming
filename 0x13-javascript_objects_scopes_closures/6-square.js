#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.width; i++) {
        let output = '';
        for (let y = 0; y < this.width; y++) {
          output += X;
        }
        console.log(output);
    } else {
      for (let i = 0; i < this.width; i++) {
        let output = '';
        for (let y = 0; y < this.width; y++) {
          output += c;
        }
        console.log(output);
      }
    }
  }
}

module.exports = Square;
