// get data from webpage
var dirtyText = document.body.innerText
var title = document.title
var index = dirtyText.indexOf(title)


// load model
import * as tf from '@tensorflow/tfjs';
// const model = await tf.loadLayersModel("downloads://getting-started/model");


// print results
console.log(document.title)
console.log(dirtyText)
console.log(index)
console.log(dirtyText.slice(index))
