$(document).ready(function (){


  // Declare size-related variables
  var scroll;  //pixels you've scrolled from top
  var docwidth = $(document).width();
  var homeHeight;  //height of div in pixels
  var aboutHeight;
  var navHeight = $('nav ul').height(); //always constant so calculate now


  // Change background of nav bar past home section, and add hover colors
  $(window).scroll(function() { // Execute each time you scroll
    scroll = $(window).scrollTop();
    homeHeight = $('#home').height();
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
  });


  // Active Navigation
  $(window).scroll(function() {
    scroll = $(window).scrollTop();
    homeHeight = $("#home").height();
    aboutHeight = $("#about").height();
    var distanceFromBottom = $(document).height() - scroll - $(window).height();
    if (scroll < homeHeight-navHeight-50) {
      if (scroll <= 100) {
        $('nav ul #home-nav').removeClass('active-grey')
        $('nav ul #home-nav').addClass('active-white');
      } else {
        $('nav ul #home-nav').addClass('active-white')
        $('nav ul #home-nav').addClass('active-grey');
      }
    } else {
      $('nav ul #home-nav').removeClass('active-white');
      $('nav ul #home-nav').removeClass('active-grey');
    }
    if (scroll >= homeHeight-navHeight-50 && scroll < homeHeight+aboutHeight-navHeight) {
      $('nav ul #about-nav').addClass('active-grey');
    } else {
      $('nav ul #about-nav').removeClass('active-grey');
    }
    if (scroll >= homeHeight+aboutHeight-navHeight && distanceFromBottom > 0) {
      $('nav ul #projects-nav').addClass('active-grey');
    } else {
      $('nav ul #projects-nav').removeClass('active-grey');
    }
    if (distanceFromBottom == 0) {
      $('nav ul #contact-nav').addClass('active-grey');
    } else {
      $('nav ul #contact-nav').removeClass('active-grey');
    }
  });


  // Scrolling
  $('#about-nav').click(function () {
    $('html, body').animate({
      scrollTop: $('#about').offset().top - navHeight/2
    }, 750);
    return false;
  });
  $('#projects-nav').click(function (){
    $('html, body').animate({
      scrollTop: $('#projects').offset().top - navHeight
    }, 750);
    return false;
  });
  $('#contact-nav').click(function (){
    $('html, body').animate({
      scrollTop: $('#contact').offset().top
    }, 750);
    return false;
  });
  $('#home-nav').click(function (){
    $('html, body').animate({
      scrollTop: $('#home').offset().top
    }, 750);
    return false;
  });


});
