#!/usr/bin/node
const data = require('./100-data.js');
console.log(data.list);
let n = [];
for (let i = 0; i < data.list.length; i++) {
  n.push(data.list[i] * i);
}
console.log(n);
