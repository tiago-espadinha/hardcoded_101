# Proxy Pattern

## Problem it Solves
The Proxy pattern provides a surrogate or placeholder for another object to control access to it. This can be used for several purposes:
- **Virtual Proxy**: Lazy loading of expensive objects.
- **Protection Proxy**: Controlling access to an object based on permissions.
- **Remote Proxy**: Representing an object that exists in a different address space.
- **Caching Proxy**: Storing results of expensive operations.
- **Logging/Monitoring Proxy**: Adding behavior before/after access.

## UML Description
- **Subject**: Defines the common interface for RealSubject and Proxy.
- **RealSubject**: Defines the real object that the proxy represents.
- **Proxy**: Maintains a reference that lets the proxy access the RealSubject. It also implements the same interface as Subject so that it can substitute the real subject.

## When to Use
- When you need a more versatile or sophisticated reference to an object than a simple pointer.
- When an object is expensive to create or access (lazy loading).
- When you need to control access to an object (permissions).
- When you want to cache the results of expensive operations.

## When NOT to Use
- When the overhead of the proxy is not justified by the benefits.
- When direct access to the object is necessary for performance-critical code.
- When the proxy's interface diverges from the real subject's interface, causing confusion.

## Trade-offs
### Pros
- **Separation of Concerns**: The proxy can handle auxiliary tasks like caching or security without cluttering the real subject's code.
- **Performance**: Can improve performance through lazy loading or caching.
- **Security**: Can provide a layer of protection for sensitive objects.

### Cons
- **Indirection**: Adds another layer of complexity and potential latency.
- **Complexity**: Implementing a proxy that perfectly mimics the real subject's behavior can be difficult.
