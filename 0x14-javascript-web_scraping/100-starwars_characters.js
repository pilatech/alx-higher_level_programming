#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, 'utf8', function (err, res, body) {
  if (err) console.log(err);
  const film = JSON.parse(body);
  for (const actorUrl of film.characters) {
    request.get(actorUrl, 'utf8', function (err, res, body) {
      if (err) console.log(err);
      const actor = JSON.parse(body);
      console.log(actor.name);
    });
  }
});
