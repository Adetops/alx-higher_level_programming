#!/usr/bin/node

function factorial (num) {
  let i = num;
  if (num <= 1) {
    i = 1;
  } else {
    i = num * factorial(num - 1);
  }
  return i;
}

const args = process.argv.slice(2);
const myNumber = Number(args[0]);

if (typeof (myNumber) === 'number' && !isNaN(myNumber)) {
  console.log(factorial(myNumber));
} else {
  console.log(factorial(1));
}
