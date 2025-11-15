import React from 'react';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import './index.css';

export default function Home() {
  return (
    <main style={{padding: '48px', maxWidth: 1000, margin: '0 auto'}}>
      <header>
        <img src={useBaseUrl('/static/assets/alance-logo-placeholder.svg')} alt="Alance" style={{width:92}}/>
        <h1 style={{fontSize: '3rem', margin: '0.25rem 0'}}>Alance Developer Kit</h1>
        <p style={{fontSize: '1.125rem', color: 'var(--ifm-color-gray-300)'}}>
          Build and run quantum + AI applications with a hardware-agnostic SDK, runtime, and examples.
        </p>
      </header>

      <section style={{marginTop: 30}}>
        <h2>Quick start</h2>
        <p>Pick one of the quick paths below:</p>
        <ul>
          <li><Link to="getting-started">Getting started (install & hello circuit)</Link></li>
          <li><Link to="examples">Examples & notebooks</Link></li>
          <li><Link to="api-reference">API Reference</Link></li>
        </ul>
      </section>

      <section style={{marginTop: 40}}>
        <h2>Why Alance?</h2>
        <p>
          Alance aims to be the “Android for Quantum Computers” — a developer-first, open,
          hardware-agnostic stack that makes it simple to prototype, test, and deploy
          quantum-assisted algorithms for simulation, optimization, and hybrid AI.
        </p>
        <Link to="alance-sdk" className="button">Learn more →</Link>
      </section>
    </main>
  );
}
