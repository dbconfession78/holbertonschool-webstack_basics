#!/usr/bin/node
const arg = process.argv.slice(2)[0];
if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
