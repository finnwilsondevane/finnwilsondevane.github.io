(function () {
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Scroll reveal — fade/rise elements into place the first time they enter the viewport.
  var revealItems = document.querySelectorAll('.reveal');
  if (revealItems.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      revealItems.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
      revealItems.forEach(function (el) { observer.observe(el); });
    }
  }

  // Hero parallax — the mountain art drifts slightly slower than the page as you scroll past it.
  var hero = document.querySelector('.hero-scenic');
  var heroBg = document.querySelector('.hero-bg');
  if (hero && heroBg && !reduceMotion) {
    var ticking = false;
    var update = function () {
      var y = Math.max(0, Math.min(window.scrollY, hero.offsetHeight));
      heroBg.style.transform = 'translateY(' + (y * 0.12) + 'px)';
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }, { passive: true });
  }
})();
