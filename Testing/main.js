// get data from webpage
var dirtyText = document.body.innerText;
var title = document.title;
var index = dirtyText.indexOf(title);

// print results
console.log(document.title);
console.log(dirtyText);
console.log(index);
console.log(dirtyText.slice(index));
