chrome.runtime.onMessage.addListener((msg, sender, response) => {

  if(msg.name == "fake"){


    const apiKey = 'your-api-key';


    var storedWord = localStorage.getItem('wordFetch');
    var storedDesc = localStorage.getItem('descFetch');

    if(1 == 1){
      //Response
      response({word: storedWord, desc: storedDesc});
    }else{
      const apiCall = 'https://api.wordnik.com/v4/words.json/wordOfTheDay?date='+dateStr+'&api_key='+apiKey;
      console.log(apiCall);
      //We call api..
      fetch(apiCall).then(function(res) {
        //wait for response..
        if (res.status !== 200) {
          response({word: 'Error', desc: 'There was a problem loading the word of the day'});
          return;
        }
        res.json().then(function(data) {
          //send the response...
          localStorage.setItem('dayFetch', dateStr);
          localStorage.setItem('wordFetch', data.word);
          localStorage.setItem('descFetch', data.note);
          //Response
          response({word: data.word, desc: data.note});
        });
      }).catch(function(err) {
        response({word: 'Error', desc: 'There was a problem loading the word of the day'});
      });
    }

  }

  return true;

});