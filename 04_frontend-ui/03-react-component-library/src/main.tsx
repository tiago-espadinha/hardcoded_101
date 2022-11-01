import React from 'react';
import { createRoot } from 'react-dom/client';
import { Badge, Button, Input } from './index';
import './tokens/colors.css';
import './tokens/spacing.css';
import './tokens/typography.css';
import './demo.css';

const Demo = () => (
  <main className="demo">
    <header className="demo__header">
      <div>
        <p className="demo__eyebrow">Pulsar UI</p>
        <h1>Components that keep their orbit.</h1>
        <p className="demo__intro">A small, accessible React component library built for expressive interfaces.</p>
      </div>
      <Badge variant="success">Ready</Badge>
    </header>

    <section className="demo__panel" aria-labelledby="components-heading">
      <div className="demo__section-heading">
        <div>
          <p className="demo__eyebrow">Component lab</p>
          <h2 id="components-heading">A quick look around</h2>
        </div>
      </div>
      <div className="demo__controls">
        <label className="demo__field">
          <span>Email address</span>
          <Input type="email" placeholder="you@example.com" />
        </label>
        <div className="demo__actions">
          <Button variant="primary">Get started</Button>
          <Button variant="secondary">Explore tokens</Button>
        </div>
      </div>
    </section>
  </main>
);

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Demo />
  </React.StrictMode>,
);
