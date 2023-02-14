# Decorator Pattern

## Problem it Solves
The Decorator pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. It is often used to adhere to the Single Responsibility Principle, as it allows functionality to be divided between classes with unique areas of concern.

## UML Description
- **Component**: Defines the interface for objects that can have responsibilities added to them dynamically.
- **Concrete Component**: Defines an object to which additional responsibilities can be attached.
- **Decorator**: Maintains a reference to a Component object and defines an interface that conforms to Component's interface.
- **Concrete Decorator**: Adds responsibilities to the component.

## When to Use
- When you need to add responsibilities to individual objects dynamically and transparently, without affecting other objects.
- When you need to add responsibilities that can be withdrawn.
- When extension by sub-classing is impractical. Sometimes a large number of independent extensions are possible and would produce an explosion of subclasses to support every combination.

## When NOT to Use
- When the component interface is very complex, making it hard to implement a decorator that correctly forwards all requests.
- When you need to rely on object identity (the decorator is not the same as the decorated object).
- When the overhead of multiple decorators is too high.

## Trade-offs
### Pros
- **Flexibility**: More flexible than static inheritance. Responsibilities can be added or removed at runtime.
- **Single Responsibility Principle**: You can divide functionality into smaller, focused classes.
- **Open/Closed Principle**: You can introduce new decorators without changing existing code.

### Cons
- **Small Objects**: A decorator-based design often results in a system with many small objects that look alike, making it hard to learn and debug.
- **Complexity**: The initial configuration of the object can be complex, as you need to wrap the core component in multiple layers of decorators.
- **Ordering**: The order in which decorators are applied can sometimes be important and may lead to subtle bugs if not managed carefully.
