/**
 * counter.js — requestAnimationFrame number counting animation
 *
 * Animates stat numbers from 0 to their target value using an
 * ease-out-cubic easing function over a fixed duration.
 *
 * Triggered when the stat section enters the viewport via
 * IntersectionObserver. Respects prefers-reduced-motion.
 */

(function () {
  'use strict';

  // Ease-out cubic: decelerates as it approaches the target
  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  /**
   * Animate a single counter element from 0 to its data-target value.
   * @param {HTMLElement} el   — element whose textContent will update
   * @param {number} duration  — animation duration in milliseconds
   */
  function animateCounter(el, duration) {
    const target = parseFloat(el.dataset.target);
    const suffix = el.dataset.suffix || '';
    const decimals = el.dataset.decimals ? parseInt(el.dataset.decimals) : 0;

    const start = performance.now();

    function tick(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const easedProgress = easeOutCubic(progress);
      const current = target * easedProgress;

      el.textContent = current.toFixed(decimals) + suffix;

      if (progress < 1) {
        requestAnimationFrame(tick);
      } else {
        el.textContent = target.toFixed(decimals) + suffix;
      }
    }

    requestAnimationFrame(tick);
  }

  // ----------------------------------------------------------------
  // Trigger counters when stat items become visible
  // ----------------------------------------------------------------
  const DURATION = 1500; // ms

  // Check for reduced motion preference
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const counterObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const el = entry.target;

          if (prefersReduced) {
            // Immediately show final value
            const target = parseFloat(el.dataset.target);
            const suffix = el.dataset.suffix || '';
            const decimals = el.dataset.decimals ? parseInt(el.dataset.decimals) : 0;
            el.textContent = target.toFixed(decimals) + suffix;
          } else {
            // Stagger start slightly per index
            const idx = parseInt(el.closest('.stat-item')?.dataset.staggerIndex || '0', 10);
            setTimeout(() => animateCounter(el, DURATION), idx * 200);
          }

          counterObserver.unobserve(el);
        }
      });
    },
    { threshold: 0.5 }
  );

  document.querySelectorAll('[data-counter]').forEach((el) => {
    // Initialise text to 0 before animation
    const suffix = el.dataset.suffix || '';
    const decimals = el.dataset.decimals ? parseInt(el.dataset.decimals) : 0;
    el.textContent = (0).toFixed(decimals) + suffix;
    counterObserver.observe(el);
  });
})();
