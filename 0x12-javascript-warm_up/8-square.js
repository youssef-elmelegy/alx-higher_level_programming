#!/usr/bin/node
if ((process.argv[2]) !== undefined && !isNaN(process.argv[2])) {
  for (let y = 0; y < process.argv[2]; y++) {
    for (let x = 0; x < process.argv[2]; x++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
