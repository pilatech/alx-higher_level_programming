#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

async function getPerson (url) {
  return new Promise((resolve, reject) => {
    request.get(url, 'utf8', function (err, res, body) {
      if (err) {
        reject(err);
      }
      const data = JSON.parse(body);
      resolve(data.name);
    });
  });
}

request.get(url, 'utf8', function (err, res, body) {
  if (err) console.log(err);
  const film = JSON.parse(body);
  for (const actorUrl of film.characters) {
    getPerson(actorUrl)
      .then(person => console.log(person))
      .catch(e => console.log(e));
  }
});
