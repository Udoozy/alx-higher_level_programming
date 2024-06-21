#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const myargs = process.argv.slice(2);
const a = parseInt(myargs[0], 10);
const b = parseInt(myargs[1], 10);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  const result = add(a, b);
  console.log(result);
}
