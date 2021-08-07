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

import * as tf from './tf.js';

function getMethods(obj) {
  var result = [];
  for (var id in obj) {
    try {
      if (typeof(obj[id]) == "function") {
        result.push(id + ": " + obj[id].toString());
      }
    } catch (err) {
      result.push(id + ": inaccessible");
    }
  }
  return result;
}

alert(getMethods(tf).join("\n"));
// const model = await tf.loadLayersModel('./model.json');
