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
    inner.style.flexWrap = 'wrap';
    return;
  }

  function update() {
    const sectionTop    = section.getBoundingClientRect().top + window.scrollY;
    const sectionHeight = section.offsetHeight;
    const viewH         = window.innerHeight;

    // Scroll progress within the sticky range [0, 1]
    const scrolled  = window.scrollY - sectionTop;
    const range     = sectionHeight - viewH;
    const progress  = Math.max(0, Math.min(1, scrolled / range));

    // Max translation: inner width minus viewport width
    const innerWidth  = inner.scrollWidth;
    const maxTranslate = -(innerWidth - window.innerWidth) + 96; // 96px padding

    const translateX = progress * maxTranslate;

    inner.style.transform = `translateX(${translateX}px)`;
  }

  // Use smooth CSS transition to ease between scroll positions
  inner.style.transition = 'transform 0.15s cubic-bezier(0.0, 0.0, 0.2, 1)';

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update, { passive: true });

  update(); // initial call
})();
