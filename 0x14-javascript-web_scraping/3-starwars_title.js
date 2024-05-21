#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
