#!/usr/bin/node
const Rectangle = require('./107-rectangle').Rectangle;
function Square (size) {
  Rectangle.call(this);
  this.width = size;
  this.height = size;
}

module.exports.Square = Square;
