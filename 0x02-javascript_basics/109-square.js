#!/usr/bin/node
const Rectangle = require('./107-rectangle').Rectangle;
exports.Square = function Square (n) {
  Rectangle.call(this);
  this.width = n;
  this.height = n;
};
