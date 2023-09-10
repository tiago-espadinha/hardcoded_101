/**
 * horizontal.js — Horizontal scroll gallery
 *
 * Maps vertical scroll progress within a sticky container
 * to a horizontal translateX on the gallery inner element.
 *
 * The outer section height determines the total scroll range.
 * A CSS transition adds smoothness between scroll events.
 */

(function () {
  'use strict';

  const section = document.getElementById('h-scroll');
  const sticky  = section?.querySelector('.h-scroll-sticky');
  const inner   = section?.querySelector('.h-scroll-inner');

  if (!section || !sticky || !inner) return;

  // Skip for reduced-motion users
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    // Show a standard vertical layout instead
    section.style.height = 'auto';
    sticky.style.position = 'relative';
    sticky.style.height = 'auto';
    inner.style.flexWrap = 'wrap';
    inner.style.transform = 'none';
    return;
  }

  function update() {
    const sectionTop    = section.getBoundingClientRect().top + window.scrollY;
    const viewH         = window.innerHeight;
    const viewW         = sticky.clientWidth;
    const maxTranslate = Math.max(0, inner.scrollWidth - viewW);

    // Match the vertical scroll range to the gallery's actual horizontal travel.
    section.style.height = `${viewH + maxTranslate}px`;
    const sectionHeight = section.offsetHeight;

    // Scroll progress within the sticky range [0, 1]
    const scrolled  = window.scrollY - sectionTop;
    const range     = Math.max(1, sectionHeight - viewH);
    const progress  = Math.max(0, Math.min(1, scrolled / range));

    const translateX = progress * -maxTranslate;

    inner.style.transform = `translateX(${translateX}px)`;
  }

  // Use smooth CSS transition to ease between scroll positions
  inner.style.transition = 'transform 0.15s cubic-bezier(0.0, 0.0, 0.2, 1)';

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update, { passive: true });

  update(); // initial call
})();
