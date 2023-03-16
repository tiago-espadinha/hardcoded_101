/**
 * Observer pattern implementation mimicking DOM EventTarget
 * ES2022 Node.js environment
 */

class CustomEventTarget {
  #listeners = new Map();

  addEventListener(type, listener) {
    if (!this.#listeners.has(type)) {
      this.#listeners.set(type, new Set());
    }
    this.#listeners.get(type).add(listener);
  }

  removeEventListener(type, listener) {
    if (this.#listeners.has(type)) {
      this.#listeners.get(type).delete(listener);
    }
  }

  dispatchEvent(event) {
    const type = event.type;
    if (this.#listeners.has(type)) {
      for (const listener of this.#listeners.get(type)) {
        if (typeof listener === 'function') {
          listener.call(this, event);
        } else if (listener && typeof listener.handleEvent === 'function') {
          listener.handleEvent(event);
        }
      }
    }
    return !event.defaultPrevented;
  }
}

class CustomEvent {
  constructor(type, detail = {}) {
    this.type = type;
    this.detail = detail;
    this.defaultPrevented = false;
  }

  preventDefault() {
    this.defaultPrevented = true;
  }
}

// Demo
const target = new CustomEventTarget();

const logEvent = (event) => {
  console.log(`Event [${event.type}] received with detail:`, event.detail);
};

target.addEventListener('status_change', logEvent);
target.addEventListener('status_change', (e) => {
  if (e.detail.status === 'offline') {
    console.log("System is going offline!");
  }
});

target.dispatchEvent(new CustomEvent('status_change', { status: 'online', timestamp: Date.now() }));
target.dispatchEvent(new CustomEvent('status_change', { status: 'offline', timestamp: Date.now() }));
