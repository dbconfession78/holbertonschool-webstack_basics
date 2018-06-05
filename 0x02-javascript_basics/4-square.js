#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  const n = parseInt(args[0], 10);
  for (let i = 0; i < n; i++) {
    console.log('X'.repeat(n));
  }
}
