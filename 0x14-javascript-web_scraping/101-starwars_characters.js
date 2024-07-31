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
      const characters = movie.characters;
      printOrdered(characters, 0);
    }
  }
}

function printOrdered (arr, index) {
  if (index === arr.length) {
    return;
  }
  const url = arr[index];
  request.get({ url }, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      console.log(data.name);
      return printOrdered(arr, index + 1);
    }
  });
}
