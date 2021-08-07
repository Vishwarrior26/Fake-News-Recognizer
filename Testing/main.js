// get data from webpage


import { loadLayersModel } from './tf.js';

var dirtyText = document.body.innerText;
var title = document.title;
var index = dirtyText.indexOf(title);
var cleanerText = "";

// print results
console.log(document.title);

if (index != -1) {
  cleanerText = dirtyText.slice(index);
} else {
  cleanerText = dirtyText;
}

console.log(cleanerText);

const model =  tf.loadLayersModel('model.json');


