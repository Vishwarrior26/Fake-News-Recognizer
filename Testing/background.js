import * as tf from '@tensorflow/tfjs';
const tf = require('@tensorflow/tfjs');

chrome.browserAction.onClicked.addListener(function(tab) {
   chrome.tabs.executeScript(null, {file: "main.js"});
});
