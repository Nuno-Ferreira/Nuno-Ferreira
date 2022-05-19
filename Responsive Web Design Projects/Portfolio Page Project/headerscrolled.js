/* first try
var header = document.querySelector('header')

window.onscroll = function() {

  if (window.pageYOffset > 0) {
    header.classList.add('scrolled')
  } else {
    header.classList.remove('scrolled')
  }
}
*/

/* second try
const callback = (entries, observer) => {
  const entry = entries[0];
  const { intersectionRatio, isIntersecting } = entry;
  console.log(intersectionRatio, isIntersecting);
  const header = document.querySelector('.header');
  header.classList.toggle('.header-scrolled', !entry.isIntersecting);
}

const options = {
  //rootMargin: "-60px 0px 0px 0px",
  threshold: [1]
};

const io = new IntersectionObserver(callback, options);

const target = document.querySelector('.home-section');
io.observe(target);
*/

//third try
/*
$(document).ready(function() {
  $(window).scroll(function() {
    if($(this).scrollTop() > height) {
      $('.header').addClass('scrolled');
    } else {
      $('.header').removeClass('scrolled');
    }
  });
});
*/

// fourth try

function checkScroll() {
  var startY = $('.header').height() * 2;

  if($(window).scrollTop() > startY) {
    $('.header').addClass("scrolled");
  } else {
    $('.header').removeClass("scrolled");
  }
}

if($('.header').length > 0) {
  $(window).on("scroll load resize", function() {
    checkScroll();
  });
}
