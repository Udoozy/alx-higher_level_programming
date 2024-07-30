#!/usr/bin/node

const fileRequest = require('request');
const movieNum = process.argv[2];
const URL_API = 'https://swapi-api.hbtn.io/api/films/';

fileRequest(URL_API + movieNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
