#!/usr/bin/node

const fileRequest = require('request');
const movieNum = process.argv[2];
const urlApi = 'https://swapi-api.hbtn.io/api/films/';

fileRequest.get(urlApi + movieNum, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const responseJSON = JSON.parse(body);
  const characters = responseJSON.characters;
  for (const characterURL of characters) {
    fileRequest.get(characterURL, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
