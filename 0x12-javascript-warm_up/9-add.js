#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

if ((process.argv[2]) !== undefined && (process.argv[3]) !== undefined) {
  add(Number(process.argv[2]), Number(process.argv[3]));
} else {
  console.log('NaN');
}
