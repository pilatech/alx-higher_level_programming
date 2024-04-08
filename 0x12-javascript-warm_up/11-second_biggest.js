#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  arr = args.slice(2);
  let max = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (parseInt(arr[i]) > max) max = parseInt(arr[i]);
  }
  arr.splice(arr.indexOf(max), 1);
  arr = args.slice(2);
  let secMax = arr[0];
  for (let j = 0; j < arr.length; j++) {
    if (parseInt(arr[j]) > secMax) {
      max = parseInt(arr[j]);
    } else if (parseInt(arr[j]) === secMax) {
      arr.splice(indexOf(parseInt(arr[j]), 1));
        if (arr.length === 1)
           {
              secMax = 0;
              break;
           }
        j = 0;
    }
  }
	console.log(secMax);
}
