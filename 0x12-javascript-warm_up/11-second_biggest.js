#!/usr/bin/node
const myargs = process.argv.slice(2).map(Number);

if (myargs.length <= 1) {
  console.log(0);
} else {
  myargs.sort((a, b) => b - a);
  console.log(myargs[1]);
}
