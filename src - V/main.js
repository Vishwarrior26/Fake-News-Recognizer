
var dirtyText = document.body.innerText;
var index = dirtyText.indexOf(document.title);
var cleanerText = "";

// if (index != -1) {
//   cleanerText = dirtyText.slice(index);
// } else {
//   cleanerText = dirtyText;
// }
// cleanerText = cleanerText.replace(/\s+/g, '-').toLowerCase();
cleanerText = dirtyText.replace(/\s+/g, '-').toLowerCase();

console.log(cleanerText)
