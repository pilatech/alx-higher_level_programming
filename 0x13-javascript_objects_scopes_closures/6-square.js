#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        let line = '';
        for (let j = 0; j < this.height; j++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
