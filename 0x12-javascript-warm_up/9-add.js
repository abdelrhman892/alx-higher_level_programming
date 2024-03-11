#!/usr/bin/node
function add(a, b) {
    if (a === undefined || b == undefined) {
        console.log('NaN');
    }
    else {
        console.log(Number(a) + Number(b));
    }
}
add(process.argv[2], process.argv[3]);
