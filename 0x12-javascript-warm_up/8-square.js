#!/usr/bin/node
if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    let output = '';
    for (let y = 0; y < Number(process.argv[2]); y++) {
      output += 'x';
    }
    console.log(output);
  }
}
