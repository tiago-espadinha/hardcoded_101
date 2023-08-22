/**
 * particles.js — Canvas-based particle network system
 *
 * 80 particles float and connect with lines when within 120px.
 * Particles are repelled by the mouse cursor within 100px.
 *
 * Performance budget: ≤ 4ms per frame draw call.
 * Only animates transform/opacity-equivalent ops in Canvas 2D.
 */

(function () {
  'use strict';

  const canvas = document.getElementById('particles-canvas');
  if (!canvas) return;

  // Respect reduced-motion preference
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    canvas.style.display = 'none';
    return;
  }

  const ctx = canvas.getContext('2d');

  // ----------------------------------------------------------------
  // Config
  // ----------------------------------------------------------------
  const CONFIG = {
    count:          80,
    connectDist:    120,
    mouseDist:      100,
    mouseForce:     3,
    speed:          0.4,
    particleRadius: 2,
    color:          '124, 92, 252', // RGB for var(--clr-accent)
    lineOpacityMax: 0.3,
  };

  let W = 0, H = 0;
  let mouse = { x: -999, y: -999 };

  // ----------------------------------------------------------------
  // Particle class
  // ----------------------------------------------------------------
  class Particle {
    constructor() {
      this.reset(true);
    }

    reset(initial = false) {
      this.x  = Math.random() * W;
      this.y  = initial ? Math.random() * H : -10;
      this.vx = (Math.random() - 0.5) * CONFIG.speed;
      this.vy = (Math.random() - 0.5) * CONFIG.speed;
      this.r  = CONFIG.particleRadius + Math.random() * 1.5;
      this.opacity = 0.4 + Math.random() * 0.6;
    }

    update() {
      // Mouse repulsion
      const dx = this.x - mouse.x;
      const dy = this.y - mouse.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < CONFIG.mouseDist && dist > 0) {
        const force = (CONFIG.mouseDist - dist) / CONFIG.mouseDist;
        this.vx += (dx / dist) * force * CONFIG.mouseForce * 0.05;
        this.vy += (dy / dist) * force * CONFIG.mouseForce * 0.05;
      }

      // Apply velocity with damping
      this.vx *= 0.99;
      this.vy *= 0.99;

      // Clamp speed
      const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
      if (speed > CONFIG.speed * 3) {
        this.vx = (this.vx / speed) * CONFIG.speed * 3;
        this.vy = (this.vy / speed) * CONFIG.speed * 3;
      }

      this.x += this.vx;
      this.y += this.vy;

      // Bounce off walls
      if (this.x < 0)  { this.x = 0;  this.vx *= -1; }
      if (this.x > W)  { this.x = W;  this.vx *= -1; }
      if (this.y < 0)  { this.y = 0;  this.vy *= -1; }
      if (this.y > H)  { this.y = H;  this.vy *= -1; }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${CONFIG.color}, ${this.opacity})`;
      ctx.fill();
    }
  }

  // ----------------------------------------------------------------
  // Particle pool
  // ----------------------------------------------------------------
  let particles = [];

  function init() {
    particles = Array.from({ length: CONFIG.count }, () => new Particle());
  }

  // ----------------------------------------------------------------
  // Resize
  // ----------------------------------------------------------------
  function resize() {
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  }

  window.addEventListener('resize', resize, { passive: true });

  // ----------------------------------------------------------------
  // Mouse tracking
  // ----------------------------------------------------------------
  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  }, { passive: true });

  canvas.addEventListener('mouseleave', () => {
    mouse.x = -999;
    mouse.y = -999;
  });

  // ----------------------------------------------------------------
  // Draw loop
  // ----------------------------------------------------------------
  function draw() {
    ctx.clearRect(0, 0, W, H);

    // Draw connections
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const a = particles[i];
        const b = particles[j];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < CONFIG.connectDist) {
          const opacity = CONFIG.lineOpacityMax * (1 - dist / CONFIG.connectDist);
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = `rgba(${CONFIG.color}, ${opacity})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }

    // Update and draw particles
    particles.forEach((p) => {
      p.update();
      p.draw();
    });
  }

  // ----------------------------------------------------------------
  // Animation loop with performance guard
  // ----------------------------------------------------------------
  function loop() {
    const t0 = performance.now();
    draw();
    const elapsed = performance.now() - t0;

    // Log a warning if we exceed the 4ms budget (dev builds)
    if (elapsed > 4 && window.__MOTION_LAB_DEBUG__) {
      console.warn(`[particles] Frame budget exceeded: ${elapsed.toFixed(2)}ms`);
    }

    requestAnimationFrame(loop);
  }

  // ----------------------------------------------------------------
  // Bootstrap
  // ----------------------------------------------------------------
  resize();
  init();
  requestAnimationFrame(loop);
})();
