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
}
