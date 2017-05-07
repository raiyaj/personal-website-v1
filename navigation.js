$(document).ready(function (){


  // Declare size-related variables
  var scroll;  //pixels you've scrolled from top
  var docwidth;
  var homeHeight;  //height of div in pixels
  var aboutHeight;
  var navHeight = $('nav ul').height(); //always constant so calculate now


  // Change background of nav bar past home section, and add hover colors
  $(window).scroll(function() { // Execute each time you scroll
    scroll = $(window).scrollTop();
    homeHeight = $('#home').height();
    if ($(document).width() >= 800) {
      if (scroll > 100) { // if you've scrolled further than the height of div
        $('nav').css('background','rgba(242,242,242,0.9)');
        $('nav ul li a').css({
          'color': '#878787',
          'padding': '15px 13px 7px 13px'
        });
      } else {
        $('nav').css('background','none');
        $('nav ul li a').css({
          'color': 'white',
          'padding': '35px 13px 7px 13px'
        });
      }
    }
  });


  // Active navigation for desktop
  $(window).scroll(function() {
    scroll = $(window).scrollTop();
    homeHeight = $("#home").height();
    aboutHeight = $("#about").height();
    var distanceFromBottom = $(document).height() - scroll - $(window).height();
    if ($(document).width() >= 800) {
      if (scroll < homeHeight-75) {
        if (scroll <= 100) {
          $('nav ul #home-nav').removeClass('active-grey');
          $('nav ul #home-nav').addClass('active-white');
        } else {
          $('nav ul #home-nav').addClass('active-white');
          $('nav ul #home-nav').addClass('active-grey');
        }
      } else {
        $('nav ul #home-nav').removeClass('active-white');
        $('nav ul #home-nav').removeClass('active-grey');
      }
      if (scroll >= homeHeight-75 && scroll < homeHeight+aboutHeight+60) {
        $('nav ul #about-nav').addClass('active-grey');
      } else {
        $('nav ul #about-nav').removeClass('active-grey');
      }
      if (scroll >= homeHeight+aboutHeight+60) {
        $('nav ul #projects-nav').addClass('active-grey');
      } else {
        $('nav ul #projects-nav').removeClass('active-grey');
      }
      if (distanceFromBottom == 0) {
        $('nav ul #about-nav').removeClass('active-grey');
        $('nav ul #projects-nav').addClass('active-grey');
      }
    }
  });


  // Scrolling (desktop)
  $('#about-nav').click(function () {
    $('html, body').animate({
      scrollTop: $('#about').offset().top
    }, 750);
    return false;
  });
  $('#projects-nav').click(function (){
    $('html, body').animate({
      scrollTop: $('#projects').offset().top - 8
    }, 750);
    return false;
  });
  $('#home-nav').click(function (){
    $('html, body').animate({
      scrollTop: $('#home').offset().top
    }, 750);
    return false;
  });


  // Scrolling (mobile)
  $('a #about-nav').click(function() {
    $('.nav-mobile').slideToggle('medium');  // close menu
    $('html, body').animate({
      scrollTop: $('#about').offset().top
    }, 750);
    return false;
  });
  $('a #projects-nav').click(function() {
    $('.nav-mobile').slideToggle('medium');
    $('html, body').animate({
      scrollTop: $('#projects').offset().top - 8
    }, 750);
    return false;
  });
  $('a #home-nav').click(function() {
    $('.nav-mobile').slideToggle('medium');
    $('html, body').animate({
      scrollTop: $('#home').offset().top
    }, 750);
    return false;
  });


  // Hamburger menu toggle for mobile
  $('.nav-mobile').hide();
  $('.handle').click(function() {
    $('.nav-mobile').slideToggle('slow');
  });


});
