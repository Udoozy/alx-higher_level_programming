#!/usr/bin/node
const myArgs = process.argv.slice(2);
const x = parseInt(myArgs[0], 10);
let i;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
