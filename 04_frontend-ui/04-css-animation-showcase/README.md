# Motion Lab: CSS Animation Showcase

A high-performance CSS animation showcase demonstrating advanced scroll-driven effects, morphing shapes, particle systems, and GPU-composited transitions — all without animation libraries.

## Features

- **Text Reveal Hero**: Letter-by-letter staggered headline animation with animated gradient mesh background
- **Scroll-Triggered Cards**: IntersectionObserver-powered feature cards with staggered entrance animations
- **SVG Path Drawing**: Self-drawing circuit-board illustration driven by `stroke-dashoffset`
- **Morphing Blobs**: Four organic shapes continuously morphing via CSS `clip-path` keyframes
- **Number Counter**: `requestAnimationFrame`-based counters with ease-out-cubic interpolation
- **Horizontal Scroll Gallery**: Vertical scroll mapped to horizontal translation for a smooth gallery experience
- **Cursor Follow**: Laggy glowing cursor tracker using linear interpolation (lerp)
- **Particle System**: Canvas-based 80-particle network that reacts to mouse proximity

## Learning Objectives

- Know which CSS properties trigger layout, paint, or composite — and why it matters
- Use IntersectionObserver confidently for scroll-driven effects
- Implement smooth interpolation (lerp) and easing functions by hand

## Project Structure

```
motion-lab/
├── index.html              # Main page with all sections
├── css/
│   ├── variables.css       # Design tokens and CSS custom properties
│   ├── base.css            # Reset and base typography
│   ├── layout.css          # Section and grid layout
│   └── animations.css      # All @keyframes declarations
├── js/
│   ├── scroll.js           # IntersectionObserver scroll triggers
│   ├── cursor.js           # Lerp-based cursor follow effect
│   ├── counter.js          # rAF number counting animation
│   ├── horizontal.js       # Horizontal scroll gallery mapping
│   └── particles.js        # Canvas particle system
└── assets/
    └── hero.svg            # Circuit board SVG illustration
```

## Requirements

- Any modern browser (Chrome 90+, Firefox 88+, Safari 14+)
- No build step required — open `index.html` directly or serve with any static server

## How to Run

Open directly in a browser:
```bash
open index.html
```

Or serve with Python's built-in server:
```bash
python -m http.server 8080
# then visit http://localhost:8080
```

## Testing

Open Chrome DevTools → Performance panel and record a scroll session. All animations should hold a stable **60fps**. The particle system targets a ≤4ms draw budget per frame — verify in the Canvas tab.

Check accessibility: toggle `prefers-reduced-motion` in DevTools → Rendering to confirm all animations disable gracefully.
