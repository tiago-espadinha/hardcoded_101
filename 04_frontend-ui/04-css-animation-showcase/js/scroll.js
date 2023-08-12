/**
 * scroll.js — IntersectionObserver scroll trigger logic
 *
 * Observes elements and adds .visible class on entry.
 * Supports staggered delays via data-stagger-index attribute.
 */

(function () {
  'use strict';

  // ----------------------------------------------------------------
  // Feature cards — staggered entrance
  // ----------------------------------------------------------------
  const STAGGER_DELAY_MS = 100;

  const cardObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const idx = parseInt(el.dataset.staggerIndex || '0', 10);
          el.style.transitionDelay = `${idx * STAGGER_DELAY_MS}ms`;
          el.classList.add('visible');
          cardObserver.unobserve(el);
        }
      });
    },
    { threshold: 0.15 }
  );

  document.querySelectorAll('.card').forEach((card, i) => {
    card.dataset.staggerIndex = i;
    cardObserver.observe(card);
  });

  // ----------------------------------------------------------------
  // SVG path drawing — trigger when section enters viewport
  // ----------------------------------------------------------------
  const svgObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          svgObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  document.querySelectorAll('.svg-wrapper').forEach((el) => {
    svgObserver.observe(el);
  });

  // ----------------------------------------------------------------
  // Stat items — staggered entrance
  // ----------------------------------------------------------------
  const statObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const idx = parseInt(el.dataset.staggerIndex || '0', 10);
          el.style.transitionDelay = `${idx * 150}ms`;
          el.classList.add('visible');
          statObserver.unobserve(el);
        }
      });
    },
    { threshold: 0.3 }
  );

  document.querySelectorAll('.stat-item').forEach((item, i) => {
    item.dataset.staggerIndex = i;
    statObserver.observe(item);
  });

  // ----------------------------------------------------------------
  // Generic reveal — any element with data-reveal attribute
  // ----------------------------------------------------------------
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );

  document.querySelectorAll('[data-reveal]').forEach((el) => {
    revealObserver.observe(el);
  });
})();
