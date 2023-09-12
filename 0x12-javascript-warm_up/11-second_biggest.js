#!/usr/bin/node

const args = process.argv.slice(2);

function count (...args) {
  return args.reduce((count, arg) => {
    return count + 1;
  }, 0);
}

if (count(...args) <= 1) {
  console.log(0);
} else {
  let secondLargest = 0;
  for (let i = 0; i < count(...args); i++) {
    if (Number(args[i]) > Number(args[i + 1])) {
      secondLargest = args[i + 1];
    } else {
      secondLargest = args[i];
    }
  }
  console.log(secondLargest);
}
