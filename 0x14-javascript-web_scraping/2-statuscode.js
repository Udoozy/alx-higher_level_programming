#!/usr/bin/node
const Filerequest = require('request');
Filerequest.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
