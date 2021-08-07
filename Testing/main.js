// get data from webpage
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
import * as tf from '@tensorflow/tfjs';

chrome.runtime.getURL('model.json');
const model = await tf.loadLayersModel(chrome.runtime.getURL('model.json'));
