#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const filePath = args[0];
let str = '';
if (args.length >= 2) {
  str = args[1];
}
fs.writeFile(filePath, str, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
