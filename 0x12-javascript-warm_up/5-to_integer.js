#!/usr/bin/node

const args = process.argv.slice(2);

const myNumber = Number(args[0]);
if (typeof (myNumber) === 'number' && !isNaN(myNumber)) {
  console.log(`My number: ${myNumber}`);
} else {
  console.log('Not a number');
}
