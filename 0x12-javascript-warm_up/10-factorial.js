#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial (num) {
  if ((num === 1) || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(n));
