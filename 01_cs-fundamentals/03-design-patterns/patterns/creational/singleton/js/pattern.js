/**
 * EventBus Singleton
 * In JavaScript/ES2022, modules are singletons by default.
 */
class EventBus {
    #subscribers = new Map();

    subscribe(event, callback) {
        if (!this.#subscribers.has(event)) {
            this.#subscribers.set(event, []);
        }
        this.#subscribers.get(event).push(callback);
    }

    publish(event, data) {
        if (this.#subscribers.has(event)) {
            this.#subscribers.get(event).forEach(callback => callback(data));
        }
    }
}

// Export a single instance
export const eventBus = new EventBus();

// Example usage
eventBus.subscribe("user_logged_in", (user) => {
    console.log(`Welcome, ${user.name}!`);
});

eventBus.subscribe("user_logged_in", (user) => {
    console.log(`Logging login for user: ${user.id}`);
});

console.log("Publishing 'user_logged_in' event...");
eventBus.publish("user_logged_in", { id: 1, name: "Alice" });
