#!/usr/bin/node
const Rectangle = require('./107-rectangle').Rectangle;
function Square (size) {
  Rectangle.call(this, size);
  if (size > 0) {
    this.width = size;
    this.height = size;
  }
}
Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    c = 'X';
  }
  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports.Square = Square;
