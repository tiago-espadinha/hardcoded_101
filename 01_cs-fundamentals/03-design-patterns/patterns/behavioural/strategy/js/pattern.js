/**
 * Strategy pattern implementation for Payment Processing
 * ES2022 Node.js environment
 */

// Strategies
class CreditCardPayment {
  pay(amount) {
    console.log(`Paying ${amount} using Credit Card...`);
    return true;
  }
}

class PayPalPayment {
  pay(amount) {
    console.log(`Paying ${amount} using PayPal...`);
    return true;
  }
}

class CryptoPayment {
  pay(amount) {
    console.log(`Paying ${amount} using Cryptocurrency...`);
    return true;
  }
}

// Context
class Checkout {
  #strategy;

  constructor(strategy) {
    this.#strategy = strategy;
  }

  setStrategy(strategy) {
    this.#strategy = strategy;
  }

  processOrder(amount) {
    console.log(`\n--- Processing order of $${amount} ---`);
    const success = this.#strategy.pay(amount);
    
    if (success) {
      console.log("Order processed successfully!");
    } else {
      console.log("Order processing failed.");
    }
  }
}

// Client Code
const checkout = new Checkout(new CreditCardPayment());
checkout.processOrder(100);

checkout.setStrategy(new PayPalPayment());
checkout.processOrder(250);

checkout.setStrategy(new CryptoPayment());
checkout.processOrder(50);
