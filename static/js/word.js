document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".letter-about-section .word h1");

  const animateCount = (el, start, end, duration, suffix = "") => {
    let startTime = null;
    const step = (timestamp) => {
      if (!startTime) startTime = timestamp;
      const progress = Math.min((timestamp - startTime) / duration, 1);
      const value = Math.floor(progress * (end - start) + start);
      el.textContent = value + suffix;
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const h1s = entry.target.querySelectorAll("h1");

        // detect suffix from original text
        animateCount(h1s[0], 1, 6, 2000, "+");
        animateCount(h1s[1], 1, 19, 2000, "+");
        animateCount(h1s[2], 1, 200, 2000, "+");

        observer.unobserve(entry.target); // run only once
      }
    });
  }, { threshold: 0.5 });

  observer.observe(document.querySelector(".letter-about-section"));
});