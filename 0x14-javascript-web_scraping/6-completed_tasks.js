#!/usr/bin/node
const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  const options = {
    url
  };
  request.get(options, cb);

  function cb (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const completed = {};
      const todos = JSON.parse(body);
      for (const todo of todos) {
        const userId = todo.userId.toString();
        if (userId in completed && todo.completed) {
          completed[userId] += 1;
        } else if (todo.completed) {
          completed[userId] = 1;
        }
      }
      console.log(completed);
    }
  }
}
