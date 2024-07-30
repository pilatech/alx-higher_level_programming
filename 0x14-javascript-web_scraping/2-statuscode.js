#!/usr/bin/node
const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  const options = {
    url
  };
  request.get(options, cb);

  function cb (error, response, body) {
    if (error) { console.log(error); } else { console.log(`code: ${response.statusCode}`); }
  }
}
