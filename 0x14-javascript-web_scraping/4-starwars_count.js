#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const count = data.results.reduce((acc, movie) => {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      acc++;
    }
    return acc;
  }, 0);
  console.log(count);
});
