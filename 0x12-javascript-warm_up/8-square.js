#!/usr/bin/node

const args = process.argv.slice(2);

const myNumber = Number(args[0]);
if (typeof (myNumber) === 'number' && !isNaN(myNumber)) {
  for (let i = 0; i < myNumber; i++) {
    for (let i = 0; i < myNumber; i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
