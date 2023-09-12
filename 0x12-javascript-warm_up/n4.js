#!/usr/bin/node

const args = process.argv.slice(2);

function count (...args) {
  return args.reduce((count, arg) => {
    return count + 1;
  }, 0);
}

let a = args[0];
let b = args[1];
if (count(...args) < 1) {
  a = 'undefined'; b = 'undefined';
  console.log(a + ' is ' + b);
} else if (count(...args) === 1) {
  b = 'undefined';
  console.log(a + ' is ' + b);
} else {
  console.log(a + ' is ' + b);
}
