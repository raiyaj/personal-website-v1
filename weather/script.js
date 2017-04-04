$(document).ready(function() {

  //function that converts unix timestamp from api to local time, and gives 12 hr format w/ am/pm. Also returns original hour and minute value for day/night calc later on
  function timeConverter(timestamp) {
    var date = new Date(timestamp * 1000); //convert to milliseconds because JS works in ms
    var hour = date.getHours();
    var min = date.getMinutes();
    var updatedMin = min;
    if (min < 10) {
      updatedMin = "0" + min; //add 0 before minutes less than 10 so that time reads 8:05
    }
    var amORpm;
    var updatedHour = hour;
    if (hour > 12) { //if past noon, it's pm.
      amORpm = "pm";
      updatedHour = hour - 12;
    } else if (hour == 12) {
      amORpm = "pm";
    } else {
      amORpm = "am";
    }
    var formatted = updatedHour + ":" + updatedMin + amORpm;
    return [formatted,hour,min];
  };


  if (navigator.geolocation) {  //if user allows browser to detect their location
    navigator.geolocation.getCurrentPosition(function(position) { //use browser's built-in navigation

      console.log(position);  //print user's current location
      var latitude = position.coords.latitude;
      var longitude = position.coords.longitude;

      var url = "https://cors-anywhere.herokuapp.com/http://api.openweathermap.org/data/2.5/weather?lat="+latitude+"&lon="+longitude+"&units=metric&appid=eb612d5ad11c69d8a65c09add5a5fba0";

      $.getJSON(url)

      //Success
      .done(function(obj) {
        console.log(JSON.stringify(obj));  //print location's current weather

        //fade out animation once regular content has loaded
        $(".loader").fadeOut("medium");

        //sunrise and sunset
        var sunriseData = timeConverter(obj.sys.sunrise);
        var sunsetData = timeConverter(obj.sys.sunset);
        var sunriseSunsetStr = 'SUNRISE<span class="time sunrise"> &nbsp; ' + sunriseData[0] + ' </span> &nbsp; &nbsp; &nbsp;SUNSET<span class="time sunset"> &nbsp; ' + sunsetData[0] + ' </span>';
        $(".sunriseSunset").html(sunriseSunsetStr);

        //Get weather and description
        var descripCode = '<span class="description"> &nbsp; (' + obj.weather[0].description + ')</span>';
        $(".weather").html(obj.weather[0].main + descripCode);

        //Get owfont icon
        var weatherId = obj.weather[0].id;
        var currentTime = position.timestamp;
        var currentTimeData = timeConverter(currentTime / 1000);  //divide by 1000 bc geolocator gives timestamp in ms, and is going to be converted to ms in timeConverter()
        var dayORnight;
        if (currentTimeData[1] == sunriseData[1] && currentTimeData[2] >= sunriseData[2]) {
          dayORnight = "-d"; //current hour equal to sunrise hour and current min >= sunrise min
        } else if (currentTimeData[1] > sunriseData[1] && currentTimeData[1] < sunsetData[1]) {
          dayORnight = "-d"; //sunrise hour < current hour < sunset hour
        } else if (currentTimeData[1] == sunsetData[1] && currentTimeData[2] < sunsetData[2]){
          dayORnight = "-d"; //current hour equal to sunset hour and current min < sunset min
        } else {
          dayORnight = "-n";
        }
        $(".owf").addClass("owf-" + weatherId + dayORnight);



        console.log(sunriseData);
        console.log(sunsetData);
        console.log(currentTimeData);

        //Get city and country
        $(".city-country").html(obj.name+", "+obj.sys.country);

        //Get temperatures
        var tempCelsius = Math.round(obj.main.temp);
        var tempFahrenheit = Math.round(tempCelsius * 1.8 + 32);
        $(".temp").html(tempCelsius+" &deg;C"); //default is Celsius

        //Toggling between Fahrenheit and Celsius
        $(".switch").append('<div class="switch-btn">&deg;C &nbsp &nbsp &nbsp &deg;F</div>');
        var checkboxOddEven = 0;
        $("input").change(function() {
          checkboxOddEven+=1;
          if (checkboxOddEven % 2 == 1) {
            $(".temp").html(tempFahrenheit+" &deg;F");
          } else {
            $(".temp").html(tempCelsius+" &deg;C");
          }
        });



      })

      //Error
      .fail(function(jqxhr,testStatus,error) {
        console.log("getJSON request failed: "+testStatus+error);
      });

    });

  } else {
    console.log("Geolocation is not supported by this browser.");
    alert("Sorry, unable to find your current location!");
  };


});
