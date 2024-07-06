#!/usr/bin/node

let fs = require('fs');
let request = require('request');
let args = process.argv.slice(2);
let arrUserId = [];
let arrId = [];

let obj = {};
request(args[0], function (error, response, body) {
    if (error) console.error(error);
    else {
        let data = JSON.parse(body);
        for (let i of data){
            if (i.completed === true){
                arrUserId.push(i.userId);
            }
        }
        for (let i of data){
            if (i.completed === true){
                arrId.push(i.id);
            }
        }
        for (let i in arrUserId){
            obj[`${i}`] = arrUserId[i];
        }
        for (let i in arrId){
            obj[`${i}`] = arrId[i];
        }
        console.log(obj);
    }
});
