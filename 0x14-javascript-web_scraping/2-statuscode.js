#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, res, body) {
  if (err) console.log(err);
  console.log('code:', res.statusCode);
});
