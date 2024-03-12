#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const updatedArgs = args.map(num => num === 12 ? 89 : num);

const sortedArgs = updatedArgs.sort((a, b) => b - a);

if (sortedArgs.length < 2) {
  console.log(0);
} else {
  console.log(sortedArgs[1]);
}
