#!/usr/bin/node
const args = process.argv.slice(2);
let arrOfNum = []
const num = parseInt(args, 10);
if (args.length < 1){
    console.log(0);
} else if (args.length === 1 && num === 1){
    console.log(0);
}
else {
    const arr = []
    for (let i of args){
        const number = parseInt(i, 10);
        arr.push(number);
    }
    arr.sort()
    arrOfNum = [...new Set(arr)];
    console.log(arrOfNum)
    console.log(arrOfNum[arrOfNum.length - 2])
}
