#!/usr/bin/node

const args = process.argv.slice(2);

const myNumber = Number(args[0]);
if (typeof (myNumber) === 'number' && !isNaN(myNumber)) {
  let i = 0;
  while (i < myNumber) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
