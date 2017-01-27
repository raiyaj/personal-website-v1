$(document).ready(function (){


  //Declare scrolling-related variables
  var scroll;  //pixels you've scrolled from top
  var homeHeight;  //height of div in pixels
  var aboutHeight;
  var navHeight = $("nav ul").height(); //always constant so calculate now


  //Change background of nav bar past home section, and add hover colors
  $(window).scroll(function() { //Execute each time you scroll
    scroll = $(window).scrollTop();
    homeHeight = $("#home").height();
    if (scroll >= homeHeight - navHeight - 50) { //if you've scrolled further than the height of div
      $("nav ul").css("background","rgba(0,0,0,0.8)");
      $("nav ul li a").css("color","white");
    } else {
      $("nav ul").css("background","rgba(255,255,255,0.6)");
      $("nav ul li a").css("color","black");
    }
  });


  //Active Navigation
  $(window).scroll(function() {
    scroll = $(window).scrollTop();
    homeHeight = $("#home").height();
    aboutHeight = $("#about").height();
    var distanceFromBottom = $(document).height() - scroll - $(window).height();
    if (scroll < homeHeight-navHeight-50) {
      $("nav ul li #home-nav").addClass("active");
    } else {
      $("nav ul li #home-nav").removeClass("active");
    }
    if (scroll >= homeHeight-navHeight-50 && scroll < homeHeight+aboutHeight-navHeight) {
      $("nav ul li #about-nav").addClass("active");
    } else {
      $("nav ul li #about-nav").removeClass("active");
    }
    if (scroll >= homeHeight+aboutHeight-navHeight && distanceFromBottom > 70) {
      $("nav ul li #projects-nav").addClass("active");
    } else {
      $("nav ul li #projects-nav").removeClass("active");
    }
    if (distanceFromBottom <= 70) {
      $("nav ul li #contact-nav").addClass("active");
    } else {
      $("nav ul li #contact-nav").removeClass("active");
    }
  });


  //Scrolling
  $("#about-nav, .arrow-wrapper").click(function (){  //note jQuery selector syntax for 'or'
    $('html, body').animate({
      scrollTop: $("#about").offset().top - navHeight/2
    }, 750);
    return false;
  });
  $("#projects-nav").click(function (){
    $('html, body').animate({
      scrollTop: $("#projects").offset().top - navHeight
    }, 750);
    return false;
  });
  $("#contact-nav").click(function (){
    $('html, body').animate({
      scrollTop: $("#contact").offset().top
    }, 750);
    return false;
  });
  $("#home-nav").click(function (){
    $('html, body').animate({
      scrollTop: $("#home").offset().top
    }, 750);
    return false;
  });


  //Disable background scrolling while popup is open
  $(".pictures").on("click", function() {
    $("body").css("overflow","hidden");
  });
  $(".close").on("click", function() {
    $("body").css("overflow","auto");
  });
  if (window.location.href.indexOf("#front-end-dev") != -1 ||
  window.location.href.indexOf("#back-end-dev") != -1 ||
  window.location.href.indexOf("#mount-baker") != -1) {
  //this if statement is for when the website loads with a popup already open
    $("body").css("overflow","hidden");

  }


  //Click anywhere outside popup to close
  $(document).click(function(e) {  // 'e' is event
    if ((window.location.href.indexOf("#front-end-dev") != -1 ||
    window.location.href.indexOf("#back-end-dev") != -1 ||
    window.location.href.indexOf("#mount-baker") != -1) &&
    !$(e.target).is(".popup") && !$(e.target).parents().is(".popup")) {
    //eg. only if a popup is actually open and if
    //the event (click) is not on .popup, or on any element whose parent is .popup
      location.href = "#/";  //close popup w/o scrolling to top
      $("body").css("overflow","auto");  //enable background scrolling again
      $(".overlay").css("transition","0.4s");  //re-add overlay transition
    }
  });


  //Add fade transition to popups, except for when navigating with prev/next buttons
  $(".pictures, .close").on("click", function() {
    $(".overlay").css("transition","0.4s");
  });
  $(".prev-next").on("click", function() {
    $(".overlay").css("transition","none");
  });


});
