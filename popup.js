document.getElementById('button').addEventListener('click', fakeOrNot);

function delay(n) {
  return new Promise(function(resolve) {
    setTimeout(resolve, n * 1000);
  });
}

function fakeOrNot() {
  //TODO API stuff here
  document.getElementById("answer").innerHTML = "processing...";
  document.getElementById("percentage").innerHTML = "0%";

  var dirtyText = document.body.innerText;
  var index = dirtyText.indexOf(document.title);
  var cleanerText = "";

  cleanerText = dirtyText.replace(/\s+/g, '-').toLowerCase();

  console.log(cleanerText)
}
