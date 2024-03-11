// #!/usr/bin/node
// if (process.argv.length === 2 || isNaN(process.argv[2])) {
//   console.log('Missing size');
// } else {
//   for (let i = 0; i < Number(process.argv[2]); i++) {
//     let output = '';
//     for (let y = 0; y < Number(process.argv[2]); y++) {
//       output += 'x';
//     }
//     console.log(output);
//   }
// }
#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log("Missing size");
} else {
  for (let i = 0; i < size; i++) {
    let row = "";
    for (let j = 0; j < size; j++) {
      row += "X";
    }
    console.log(row);
  }
}
