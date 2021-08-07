// get data from webpage


import { loadLayersModel } from './tf.js';

var dirtyText = document.body.innerText;
var title = document.title;
var index = dirtyText.indexOf(title);
var cleanerText = "";

// print results
// console.log(document.title);

if (index != -1) {
  cleanerText = dirtyText.slice(index);
} else {
  cleanerText = dirtyText;
}

<<<<<<< HEAD

import * as tf from './tf.js';
const model = tf.loadLayersModel('model.json');
console.log("test")
