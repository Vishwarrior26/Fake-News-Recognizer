var dirtyText = document.body.innerText
var title = document.title
var index = dirtyText.indexOf(title)
console.log(document.title)
console.log(dirtyText)
console.log(index)
console.log(dirtyText.slice(index))
