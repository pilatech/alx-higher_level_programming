#!/usr/bin/node
const fs = require('fs');

if (process.argv.length >= 3) {
  const filename = process.argv[2];
  fs.readFile(filename, 'utf-8', (error, data) => {
    if (error) {
      console.log(error);
    } else {
      console.log(data);
    }
  });
}
