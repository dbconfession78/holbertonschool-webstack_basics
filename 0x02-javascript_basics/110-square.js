#!/usr/bin/node
const Square = require('./109-square').Square;

Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    c = 'X';
  }
  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports.Square = Square;
