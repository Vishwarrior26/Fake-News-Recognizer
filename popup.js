document.getElementById('button').addEventListener('click', fakeOrNot);

function delay(n) {
  return new Promise(function(resolve) {
    setTimeout(resolve, n * 1000);
  });
}

function fakeOrNot() {
  document.getElementById("answer").innerHTML = "processing...";
  document.getElementById("percentage").innerHTML = "0%";
  console.log("confirmation that this is running");
  var dirtyText = document.body.innerText;
  var index = dirtyText.indexOf(document.title);
  var cleanerText = "";
  cleanerText = dirtyText.replace(/\s+/g, '-').toLowerCase();
  const apiCall = "https://dry-bastion-58116.herokuapp.com/handler/"+cleanerText;
  console.log(cleanerText);
  fetch("https://still-castle-94087.herokuapp.com/"+ apiCall)
  .then((response) => {
    console.log("resolved", response);
    return response.json();
  }).then(data => {
     const jsondata = data;
     console.log(jsondata.prediction)
     if (jsondata.prediction >= 0.5) {
      document.getElementById("answer").innerHTML = "The content in this tab is not fake.";
      document.getElementById("percentage").innerHTML = "";
    } else {
      document.getElementById("answer").innerHTML = "The content in this tab is fake.";
      document.getElementById("percentage").innerHTML = "";
    }
  }).catch((err) => {
    console.log("rejected", err);
    document.getElementById("answer").innerHTML = "Unfortunately there has been an error. Please click the button again.";
    document.getElementById("percentage").innerHTML = "";
  });
  
};

