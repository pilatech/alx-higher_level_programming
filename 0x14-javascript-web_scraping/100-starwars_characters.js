#!/usr/bin/node
const request = require('request');

if (process.argv.length >= 3) {
  const movieId = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  const options = {
    url
  };
  request.get(options, cb);

  function cb (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const movie = JSON.parse(body);
      for (const characterUrl of movie.characters) {
        request.get({ url: characterUrl }, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      }
    }
  }
}
