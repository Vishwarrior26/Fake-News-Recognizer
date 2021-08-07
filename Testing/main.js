// get data from webpage
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

// console.log(cleanerText);
import './tf.js';
const model = loadLayersModel('model.json');
console.log("test")
