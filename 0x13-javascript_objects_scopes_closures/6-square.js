#!/usr/bin/node
// class Square that inherits from square

const Square1 = require('./5-square');

class Square extends Square1 {
  constructor(size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (!c) {
          process.stdout.write('X');
	} else {
          process.stdout.write(c);
	}
      }
      console.log('');
    }
  }
}

module.exports = Square;
