#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const sourceA = args[2];
const sourceB = args[3];
const dest = args[4];
let data = fs.readFileSync(sourceA, 'utf8');
data += fs.readFileSync(sourceB, 'utf8');
fs.writeFileSync(dest, data);
