#!/usr/bin/node

const args = process.argv.slice(2);

function count (...args) {
  return args.reduce((count, arg) => {
    return count + 1;
  }, 0);
}

if (count(...args) < 1) {
  console.log('No argument');
} else if (count(...args) === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
