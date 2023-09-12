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
  let secondLargest;
  let temp;
  for (let i = 0; i < count(...args) - 1; i++) {
    if (Number(args[i]) > Number(args[i + 1])) {
      temp = args[i];
      args[i] = args[i + 1];
      args[i + 1] = temp;
    }
    secondLargest = args[i];
  }
  console.log(secondLargest);
}
