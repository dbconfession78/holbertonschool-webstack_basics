#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
let n = [];
for (let i = 0; i < list.length; i++) {
  n.push(list[i] * i);
}
console.log(n);
