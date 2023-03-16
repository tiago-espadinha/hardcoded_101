/**
 * The Target interface defines the operations that all Storage adapters must implement.
 */
class StorageInterface {
    getItem(key) { throw new Error('Method not implemented'); }
    setItem(key, value) { throw new Error('Method not implemented'); }
    removeItem(key) { throw new Error('Method not implemented'); }
    clear() { throw new Error('Method not implemented'); }
}

/**
 * Mock for Web Storage API (localStorage/sessionStorage) since we are in Node.js
 */
class MockWebStorage {
    constructor() {
        this.store = {};
    }
    getItem(key) { return this.store[key] || null; }
    setItem(key, value) { this.store[key] = String(value); }
    removeItem(key) { delete this.store[key]; }
    clear() { this.store = {}; }
    get length() { return Object.keys(this.store).length; }
}

/**
 * The Adapter class that makes any Web Storage compatible with our StorageInterface.
 */
class WebStorageAdapter extends StorageInterface {
    constructor(webStorage) {
        super();
        this.webStorage = webStorage;
    }

    getItem(key) {
        return this.webStorage.getItem(key);
    }

    setItem(key, value) {
        this.webStorage.setItem(key, value);
    }

    removeItem(key) {
        this.webStorage.removeItem(key);
    }

    clear() {
        this.webStorage.clear();
    }
}

// Client Code
function saveUserData(storage, user) {
    storage.setItem('user_id', user.id);
    storage.setItem('user_name', user.name);
    console.log(`Saved user ${user.name} to storage.`);
}

function getUserName(storage) {
    return storage.getItem('user_name');
}

// Usage
const localStorageMock = new MockWebStorage();
const sessionStorageMock = new MockWebStorage();

const localAdapter = new WebStorageAdapter(localStorageMock);
const sessionAdapter = new WebStorageAdapter(sessionStorageMock);

const user = { id: 1, name: 'Alice' };

console.log('--- Using Local Storage Adapter ---');
saveUserData(localAdapter, user);
console.log('Retrieved:', getUserName(localAdapter));

console.log('\n--- Using Session Storage Adapter ---');
saveUserData(sessionAdapter, { id: 2, name: 'Bob' });
console.log('Retrieved:', getUserName(sessionAdapter));
