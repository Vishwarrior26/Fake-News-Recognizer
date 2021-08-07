// get data from webpage
var dirtyText = document.body.innerText
var title = document.title


// load model
src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest"
import * as tf from '@tensorflow/tfjs';
const model = await tf.loadLayersModel('file:///Users/siddharth/Downloads/thats-fake/model');


// print results
console.log(document.title)
console.log(dirtyText)
console.log(dirtyText.slice(index))
