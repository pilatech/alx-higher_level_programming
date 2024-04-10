#!/usr/bin/node
const PrevSquare = require('./5-square');
class Square extends PrevSquare {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let line = '';
        for (let j = 0; j < this.height; j++) {
          line += c;
        }
        console.log(line);
      }
    }
  }
}

module.exports = Square;
