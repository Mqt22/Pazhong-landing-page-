const track = document.querySelector('.testimonial-track');
const cards = document.querySelectorAll('.testimonial-card');
let index = 0;

function getVisibleCount() {
  if (window.innerWidth <= 426) return 1;   // mobile
  if (window.innerWidth <= 968) return 2;   // tablet
  return 3;                                 // desktop
}

function moveSlider() {
  const cardWidth = cards[0].offsetWidth + 20; // width + gap
  track.style.transform = `translateX(-${index * cardWidth}px)`;
}

setInterval(() => {
  const visibleCount = getVisibleCount();
  index += visibleCount;
  if (index >= cards.length) index = 0; // loop back
  moveSlider();
}, 2000);

window.addEventListener("resize", moveSlider);
moveSlider();
