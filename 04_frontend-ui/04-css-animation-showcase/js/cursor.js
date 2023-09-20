/**
 * cursor.js — Custom cursor with lerp (linear interpolation) lag
 *
 * A glowing circle follows the cursor with a slight delay using
 * linear interpolation in a requestAnimationFrame loop.
 *
 * Performance: pointer-events: none ensures zero impact on interactivity.
 * Not activated on touch devices (coarse pointer).
 */

(function () {
  'use strict';

  // Skip on touch devices
  if (window.matchMedia('(pointer: coarse)').matches) return;

  const cursor = document.getElementById('cursor');
  if (!cursor) return;

  // Current interpolated position
  let cx = window.innerWidth / 2;
  let cy = window.innerHeight / 2;

  // Target position (raw mouse)
  let tx = cx;
  let ty = cy;

  // Lerp factor — lower = more lag (0.05–0.2 is a nice range)
  const LERP = 0.1;

  let visible = false;

  // ----------------------------------------------------------------
  // Track raw mouse position
  // ----------------------------------------------------------------
  document.addEventListener('mousemove', (e) => {
    tx = e.clientX;
    ty = e.clientY;

    if (!visible) {
      cursor.classList.remove('hidden');
      visible = true;
    }
  });

  document.addEventListener('mouseleave', () => {
    cursor.classList.add('hidden');
    visible = false;
  });

  document.addEventListener('mouseenter', () => {
    cursor.classList.remove('hidden');
    visible = true;
  });

  // ----------------------------------------------------------------
  // Expand cursor on hover over interactive elements
  // ----------------------------------------------------------------
  const INTERACTIVE = 'a, button, [role="button"], input, textarea, select, label, .card, .gallery-card';

  document.addEventListener('mouseover', (e) => {
    if (e.target.closest(INTERACTIVE)) {
      cursor.classList.add('hovering');
    }
  });

  document.addEventListener('mouseout', (e) => {
    if (e.target.closest(INTERACTIVE)) {
      cursor.classList.remove('hovering');
    }
  });

  // ----------------------------------------------------------------
  // rAF animation loop — lerp towards target
  // ----------------------------------------------------------------
  function lerp(a, b, t) {
    return a + (b - a) * t;
  }

  function animate() {
    cx = lerp(cx, tx, LERP);
    cy = lerp(cy, ty, LERP);

    cursor.style.transform = `translate(${cx - cursor.offsetWidth / 2}px, ${cy - cursor.offsetHeight / 2}px)`;

    requestAnimationFrame(animate);
  }

  requestAnimationFrame(animate);
})();
