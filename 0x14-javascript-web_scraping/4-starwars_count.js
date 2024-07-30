#!/usr/bin/node
const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  const options = {
    url
  };
  request.get(options, cb);

  function cb (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const movies = JSON.parse(body).results;
      let count = 0;
      for (const movie of movies) {
        if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      }
      console.log(count);
    }
  }
}
