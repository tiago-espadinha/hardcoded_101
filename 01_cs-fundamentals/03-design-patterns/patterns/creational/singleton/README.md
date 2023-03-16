# Singleton Pattern

## Problem It Solves
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. This is useful for coordinating actions across a system where having multiple instances would lead to inconsistent state or excessive resource usage.

## UML Description
- `Singleton`: A class with a private constructor and a static `get_instance()` method (or equivalent in Python `__new__`).
- `_instance`: A private static variable that holds the single instance.

## When to use
- Managing a shared resource (Database connection pool, configuration manager, thread pool).
- Centralizing application-wide logging or event dispatching.
- Controlling access to a hardware device.

## When NOT to use
- If you don't actually need a single instance (e.g. state can be independent).
- If it introduces tight coupling (making unit testing harder).
- If it's used as a "global variable" dumping ground.

## Trade-offs
- **Pros**: Controlled access to sole instance, reduced namespace pollution (compared to globals), lazy initialization.
- **Cons**: Can mask bad design (tight coupling), hard to unit test (due to global state), potential issues in multi-threaded environments (if not handled correctly).
