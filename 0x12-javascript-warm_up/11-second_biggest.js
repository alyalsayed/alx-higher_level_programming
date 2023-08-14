#!/usr/bin/node
//A script to search the second biggest integer in the list of arguments
const mySol = process.argv;
if (mySol.length <= 3) {
  console.log(0);
} else {
  console.log(mySol.sort((x, y) => y - x).slice(3)[0]);
}
