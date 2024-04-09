#!/usr/bin/node
const dict = require('./101-data').dict;
const obj = {};
const arr = Object.entries(dict);
for (let i = 0; i < arr.length; i++) {
  const keyV = arr[i][1];
  const valK = arr[i][0];
  if (keyV in obj) {
    obj[keyV].push(valK);
  } else {
    obj[keyV] = [];
    obj[keyV].push(valK);
  }
}
console.log(obj);
