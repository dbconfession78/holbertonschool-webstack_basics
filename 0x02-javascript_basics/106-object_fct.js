#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};
console.log(myObject);

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
