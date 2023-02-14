/**
 * Decorator pattern implementation using Higher-Order Functions (HOF)
 * ES2022 Node.js environment
 */

/**
 * Higher-order function that adds a retry mechanism to an async function.
 * @param {Function} fn The async function to decorate.
 * @param {number} retries Number of retries.
 * @param {number} delay Delay between retries in ms.
 */
export function withRetry(fn, retries = 3, delay = 1000) {
  return async function(...args) {
    let lastError;
    for (let i = 0; i < retries; i++) {
      try {
        return await fn(...args);
      } catch (err) {
        lastError = err;
        console.warn(`Attempt ${i + 1}/${retries} failed: ${err.message}`);
        if (i < retries - 1) {
          await new Promise(resolve => setTimeout(resolve, delay));
        }
      }
    }
    throw lastError;
  };
}

/**
 * Higher-order function that adds a timeout to an async function.
 * @param {Function} fn The async function to decorate.
 * @param {number} ms Timeout in milliseconds.
 */
export function withTimeout(fn, ms) {
  return async function(...args) {
    const timeoutPromise = new Promise((_, reject) => {
      setTimeout(() => reject(new Error(`Function timed out after ${ms}ms`)), ms);
    });
    return Promise.race([fn(...args), timeoutPromise]);
  };
}

/**
 * Higher-order function that adds memoization (caching) to a function.
 * @param {Function} fn The function to decorate.
 */
export function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) {
      console.log(`Returning cached result for: ${key}`);
      return cache.get(key);
    }
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

// Demo usage
if (import.meta.url === `file://${process.argv[1]}` || process.argv[1]?.endsWith('pattern.js')) {
  const slowAdd = (a, b) => {
    console.log(`Adding ${a} + ${b}...`);
    return a + b;
  };

  const memoizedAdd = memoize(slowAdd);
  console.log(memoizedAdd(2, 3));
  console.log(memoizedAdd(2, 3));

  const flakyApi = async () => {
    if (Math.random() < 0.7) throw new Error("API failure");
    return { data: "Success!" };
  };

  const reliableApi = withRetry(flakyApi, 5, 100);
  reliableApi().then(console.log).catch(console.error);
}
