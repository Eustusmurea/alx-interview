#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    if (characters && characters.length > 0) {
      printCharacters(characters, 0);
    } else {
      console.log('No characters found for this movie.');
    }
  } else {
    console.error('Error fetching movie data:', error);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    } else {
      console.error('Error fetching character data:', error);
    }
  });
}

