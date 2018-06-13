#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
let n = [];
let i = 0;
list.map(elem => {
  n.push(elem * i);
  i++;
});
console.log(n);
