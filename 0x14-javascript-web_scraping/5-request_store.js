#!/usr/bin/node
const { writeFile } = require('fs/promises');
const request = require('request');

const url = process.argv[2];
const filepath = process.argv[3];
request.get(url, 'utf8', function (err, res, body) {
  if (err) console.log(err);
  const content = body.toString();

  writeFile(filepath, content, 'utf8')
    .catch(e => console.log(e));
});
