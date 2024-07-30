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
      const movieTitle = JSON.parse(body).title;
      if (movieTitle) {
        console.log(movieTitle);
      }
    }
  }
}
