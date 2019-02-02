/**
  1) Write some code to display a clock that updates every second.  It should look roughly like this:

  -------------
  |           |
  | 11:50 PM  |
  |           |
  -------------

  2) Stretch goal: Add PLUS button that increments the HOUR
  3) Stretch goal: Add MINUS button that decrements the HOUR

  You can use the render function below, or write your own code that renders the HTML.
  Feel free to use Google.
**/

function timeout() {
    setTimeout(function () {
        render()
        timeout();
    }, 1000);
}

function hoursAMPM(milHours) {
  if(milHours<12 && milHours!==0) {
    return ['' + milHours, 'AM'];
  }
  else if(milHours===0) {
    return ['12', 'AM'];
  }
  else if(milHours===12) {
    return ['12', 'PM'];
  }
  else {
    return(['' + (milHours-12), 'PM'])
  }
}

function minuteMod(minutes) {
  if(minutes<10) {
    return '0'+minutes;
  }
  else {
    return minutes;
  }
}


function render() {
  var now = new Date();
  var app = document.getElementById("app");
  var hourTime = hoursAMPM(now.getHours());
  var minuteTime = minuteMod(now.getMinutes());
  var secondTime = minuteMod(now.getSeconds());
  app.innerHTML = '' + hourTime[0] + ':' + minuteTime + ':' + secondTime + ' ' + hourTime[1];

}

timeout()