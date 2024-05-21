#!/usr/bin/node
const { readFile } = require('fs/promises');

const filepath = process.argv[2];
readFile(filepath, 'utf8')
  .then(data => console.log(data))
  .catch(err => console.log(err));
