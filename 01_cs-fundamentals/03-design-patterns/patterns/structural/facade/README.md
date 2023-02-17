# Facade Pattern

## Problem it Solves
The Facade pattern provides a simplified interface to a complex set of classes, a library, or a framework. It helps reduce the complexity of using a subsystem by providing a single, entry-level class that manages all the low-level details.

## UML Description
- **Facade**: Provides a simplified interface and knows which subsystem classes are responsible for a request.
- **Subsystem Classes**: Implement specific functionality but are complex to use directly. They have no knowledge of the facade.
- **Client**: Interacts only with the Facade, not the subsystem classes.

## When to Use
- When you want to provide a simple interface to a complex subsystem.
- When there are many dependencies between clients and the implementation classes of an abstraction.
- When you want to layer your subsystems. Use a facade to define an entry point to each subsystem level.

## When NOT to Use
- When the subsystem is simple and doesn't need a simplified interface.
- When you need to use the full functionality of the subsystem that the facade doesn't expose.
- When the facade becomes a "god object" that knows too much about every subsystem.

## Trade-offs
### Pros
- **Simplification**: Makes a complex system easier to use.
- **Decoupling**: Reduces the number of objects that clients need to interact with.
- **Maintenance**: Changes in the subsystem don't affect the client as long as the facade interface remains stable.

### Cons
- **Limited Control**: Clients might not have access to some advanced subsystem features.
- **Rigidity**: If the facade doesn't expose a specific configuration, the client might be forced to bypass it.
