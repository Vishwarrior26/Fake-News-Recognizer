var dirtyText = document.body.innerText;
var index = dirtyText.indexOf(title);
var cleanerText = "";

if (index != -1) {
  cleanerText = dirtyText.slice(index);
} else {
  cleanerText = dirtyText;
}
