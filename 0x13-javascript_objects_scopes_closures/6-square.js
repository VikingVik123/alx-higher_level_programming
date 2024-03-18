#!/usr/bin/node

const Parent = require('./5-square.js');

class Square extends Parent {
    charPrint(c) {
        if (c === undefined) {
            c = 'X';
        }
        for (let i = 0; i < this.width; i++) {
            console.log(c.repeat(this.width));
        }
    }
}

module.exports = Square;
