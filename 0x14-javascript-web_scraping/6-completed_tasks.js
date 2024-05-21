#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, 'utf8', function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const completed = data.filter(todo => todo.completed)
    .map(todo => todo.userId);
  const stats = {};
  for (const item of completed) {
    item in stats ? stats[item]++ : stats[item] = 1;
  }
  console.log(stats);
});
