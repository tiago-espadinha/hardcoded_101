/**
 * Proxy pattern implementation using ES6 Proxy
 * Used for validation and change tracking.
 * ES2022 Node.js environment
 */

const userSchema = {
  id: "number",
  username: "string",
  age: "number",
  email: "string"
};

/**
 * Creates a proxy for an object that validates property updates against a schema.
 * @param {Object} target The object to protect.
 */
function createValidatedProxy(target) {
  return new Proxy(target, {
    set(obj, prop, value) {
      if (prop in userSchema) {
        if (typeof value !== userSchema[prop]) {
          throw new TypeError(`Invalid type for property ${prop}. Expected ${userSchema[prop]}, got ${typeof value}`);
        }
        
        if (prop === 'age' && (value < 0 || value > 120)) {
          throw new RangeError("Age must be between 0 and 120");
        }
        
        if (prop === 'email' && !value.includes('@')) {
          throw new Error("Invalid email format");
        }
      }
      
      console.log(`Proxy: setting ${prop} = ${value}`);
      obj[prop] = value;
      return true;
    },
    
    get(obj, prop) {
      console.log(`Proxy: accessing property ${prop}`);
      return obj[prop];
    }
  });
}

// Client Code
const rawUser = { id: 1, username: "jdoe", age: 30, email: "john@example.com" };
const userProxy = createValidatedProxy(rawUser);

try {
  userProxy.age = 35; // Success
  console.log(`User age: ${userProxy.age}`);
  
  userProxy.age = 150; // Throws RangeError
} catch (err) {
  console.error(`Caught error: ${err.message}`);
}

try {
  userProxy.email = "not-an-email"; // Throws Error
} catch (err) {
  console.error(`Caught error: ${err.message}`);
}

try {
  userProxy.username = 123; // Throws TypeError
} catch (err) {
  console.error(`Caught error: ${err.message}`);
}
