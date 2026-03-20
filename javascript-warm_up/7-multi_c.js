#!/usr/bin/node
const args = process.argv.slice(2);
const data = args[0];
if (isNaN(Number(data))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < data; i++) {
    console.log('C is fun');
  }
}
