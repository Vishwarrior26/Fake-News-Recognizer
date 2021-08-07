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
// console.log(cleanerText);
import * as tf from './tf.js';
const model = tf.loadLayersModel('model.json');
console.log("test")
=======
console.log(cleanerText);

const model =  tf.loadLayersModel('model.json');


>>>>>>> e341d19fcae3c6b7708a940a4c09a1ef0d976fa3
