#!/usr/bin/node
const fileRequest = require('request');
fileRequest(process.argv[2], function (error, response, body) {
  if (!error) {
    const apiResult = JSON.parse(body).apiResult;
    console.log(apiResult.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
