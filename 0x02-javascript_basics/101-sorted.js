#!/usr/bin/node
const dict = require('./101-data.js').dict;
console.log(dict);
let d = {};
const keys = Object.keys(dict);
for (let i = 0; i < keys.length; i++) {
  const key = keys[i];
  const val = dict[keys[i]];
  if (val in d) {
    d[val].push(key);
  } else {
    d[val] = [key];
  }
}
console.log(d);
