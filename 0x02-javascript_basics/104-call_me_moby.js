#!/usr/bin/node
/* Write a function that executes x times a function.

The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var */
const callMeMoby = function (n, cb) {
  for (let i = 0; i < n; i++) {
    cb();
  }
};
exports.callMeMoby = callMeMoby;
