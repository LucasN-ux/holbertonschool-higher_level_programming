#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
const myObject2 = myObject;
myObject2.value = 89;
console.log(myObject);
