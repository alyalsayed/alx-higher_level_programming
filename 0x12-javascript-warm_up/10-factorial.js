#!/usr/bin/node
//A script to compute and print a factorial of a number .
const argv = parseInt(process.argv[2]);
function factorial(num) {
  if ((Number.isNaN(num)) || (num === 1)) {
    return 1;
  }
  return factorial(num - 1) * num;
}
console.log(factorial(argv));
