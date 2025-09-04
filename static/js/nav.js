// const hamburger = document.querySelector('.hamburger');
// const nav = document.querySelector('nav>ul');
// const cta = document.querySelector('header>button');
// hamburger.addEventListener('click', ()=>{
//     nav.classList.toggle('active');
//     cta.classList.toggle('active');
// });
// const hamburger = document.querySelector('.hamburger');
// const nav = document.querySelector('nav');
// const nav_link = document.querySelector('nav>ul');
// hamburger.addEventListener('click', ()=>{
//     nav.classList.toggle('active');
//     nav_link.classList.toggle('active');
// });
  const hamburger = document.querySelector(".hamburger");
  const navMenu = document.querySelector("header nav ul");
const cta = document.querySelector("header button");
  hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("active");
    cta.classList.toggle("active");
  });
