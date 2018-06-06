#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');

fs.readFile(args[0], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  const a = data;
  fs.readFile(args[1], 'utf8', function (err, data) {
    if (err) {
      console.log(err);
      process.exit(1);
    }

    const b = data;
    fs.writeFile(args[2], a + b, function (err) {
      if (err) {
        console.log(err);
        process.exit(1);
      }
    });
  });
});
