#!/usr/bin/node
const oc = parseInt(process.argv[2]);
if (isNaN(oc)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < oc; i++) {
    console.log('C is fun');
  }
}
