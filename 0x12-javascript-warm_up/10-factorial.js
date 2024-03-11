#!/usr/bin/node
function Factorial (a) {
  let num = 1;
  if (a === undefined || isNaN(a)) {
    console.log(1);
  } else {
    for (let i = 1; i <= a; i++) {
      num *= i;
    }
    console.log(num);
  }
}

Factorial(process.argv[2]);
