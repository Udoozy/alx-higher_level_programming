#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, argContent) {
  console.log(error || argContent);
});
