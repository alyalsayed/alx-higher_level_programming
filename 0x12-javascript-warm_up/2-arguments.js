#!/usr/bin/node
/*
A script to print a message depending
on the number of arguments .
*/
const numArgv = process.argv.length;
if (numArgv < 3) {
  console.log('No argument');
} else if (numArgv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
