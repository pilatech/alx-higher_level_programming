#!/usr/bin/node
const { writeFile } = require('fs/promises');

const filepath = process.argv[2];
const content = process.argv[3];
writeFile(filepath, content, 'utf8')
  .catch(err => console.log(err));
