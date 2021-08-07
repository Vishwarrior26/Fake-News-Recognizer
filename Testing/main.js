// get data from webpage
var dirtyText = document.body.innerText;
var title = document.title;
var index = dirtyText.indexOf(title);
var cleanerText = "";
// print results
console.log(document.title);
// console.log(dirtyText);
// console.log(index);
// console.log(dirtyText.slice(index));

if (index != -1){
  cleanerText = dirtyText.slice(index);
}
else {
  cleanerText = dirtyText;
}

console.log(cleanerText);
