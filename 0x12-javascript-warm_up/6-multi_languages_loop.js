#!/usr/bin/node

const myArr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
while (typeof (myArr[0]) !== 'undefined') {
  console.log(myArr.shift());
}
