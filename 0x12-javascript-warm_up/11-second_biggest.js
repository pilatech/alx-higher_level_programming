#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const arr = args.slice(2).map(item => parseInt(item));
  const max = Math.max(...arr);
  const newArr = arr.filter(item => item !== max);
  if (newArr.length === 0) {
    console.log(0);
  } else {
    const secondMax = Math.max(...newArr);
    console.log(secondMax);
  }
}
