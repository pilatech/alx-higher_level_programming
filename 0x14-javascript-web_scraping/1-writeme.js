#!/usr/bin/node
const fs = require('fs');

if (process.argv.length >= 4) {
  const filename = process.argv[2];
  const str = process.argv[3];
  fs.writeFile(filename, str, 'utf-8', (error) => {
    if (error) { console.log(error); }
  });
}
