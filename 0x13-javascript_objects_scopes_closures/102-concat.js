#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const sourceA = args[2];
const sourceB = args[3];
const dest = args[4];
let info = '';
fs.readFile('fileA','utf8', (err, data) => {
	if (err) throw err;
	info += data;
})
fs.readFile('fileB', 'utf8', (err, data) => {
	if (err) throw err;
	info += data;
})

console.log(info);
