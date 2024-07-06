#!/usr/bin/node

const request = require('request');
let count = 0;
let argv = process.argv.splice(2);

if (argv.length < 1) {
    console.error("There is no movie ID");
} else {
    request(argv[0], (error, response, body) => {
        if (error) {
            console.error("Error: ", error);
        } else {
           let bodyToObject = JSON.parse(body);
           for (let key of bodyToObject.results) {
                for (let i of key["characters"]) {
                    let arr = i.split("/");
                    if (arr[arr.length - 2] === "18") {
                        count++;
                    }
                }
           }
           console.log(count)
        }
    })
}
