/*var header = document.querySelector('header')

window.onscroll = function() {

  if (window.pageYOffset > 0) {
    header.classList.add('scrolled')
  } else {
    header.classList.remove('scrolled')
  }
}
*/

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
