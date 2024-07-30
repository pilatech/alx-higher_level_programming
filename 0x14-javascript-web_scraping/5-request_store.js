#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length >= 4) {
  const url = process.argv[2];
  const filepath = process.argv[3];
  const options = {
    url
  };
  request.get(options, cb);

  function cb (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      fs.writeFile(filepath, body, 'utf-8', (error) => {
        if (error) {
          console.log(error);
        }
      });
    }
  }
}
