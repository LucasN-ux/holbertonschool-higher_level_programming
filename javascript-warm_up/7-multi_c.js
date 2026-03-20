#!/usr/bin/node
const x = process.argv.slice(2);
if (x.length === 0 ) {
  console.log('Missing number of occurrences');
} else {
  const n = parseInt(x[0]);
  if (isNaN(n)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < n; i++) {
      console.log('C is fun');
    }
  }
}
