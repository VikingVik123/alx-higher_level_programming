#!/usr/bin/node

function factorial (n) {
  // Base case
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  }

  // Recursive case
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
