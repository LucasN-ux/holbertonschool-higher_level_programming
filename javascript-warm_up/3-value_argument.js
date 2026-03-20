#!/usr/bin/node
const args = process.argv.slice(2);
const name = args[0];
if (name) {
  console.log(`${name}`);
} else {
  console.log('NO argument');
}
