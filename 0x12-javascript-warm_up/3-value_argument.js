#!/usr/bin/node
// if (!arg1 || !arg2) {
//   console.log('No argument');
// } else {
//   console.log(process.argv[2]);
// }
const [arg] = process.argv.slice(2);

if (arg === undefined) {
  console.log("No argument");
} else {
  console.log(arg);
}
