#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // create an empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let length = '';
      for (let x = 0; x < this.width; x++) {
        length += 'X';
      }
      console.log(length);
    }
  }
}

module.exports = Rectangle;
