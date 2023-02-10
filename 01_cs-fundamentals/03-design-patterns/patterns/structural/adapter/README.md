# Adapter Pattern

## Problem it Solves
The Adapter pattern allows objects with incompatible interfaces to collaborate. It's particularly useful when you want to use an existing class, but its interface doesn't match the one you need, or when you want to create a reusable class that cooperates with unrelated or unforeseen classes.

## UML Description
- **Target**: Defines the domain-specific interface that Client uses.
- **Client**: Collaborates with objects conforming to the Target interface.
- **Adaptee**: Defines an existing interface that needs adapting.
- **Adapter**: Adapts the interface of Adaptee to the Target interface.

## When to Use
- When you want to use an existing class, and its interface does not match the one you need.
- When you want to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don't necessarily have compatible interfaces.
- (Object adapter only) When you need to use several existing subclasses, but it's impractical to adapt their interface by sub-classing every one. An object adapter can adapt the interface of its parent class.

## When NOT to Use
- If you have control over the source code of both classes, it might be better to refactor them to use a common interface instead of adding a layer of complexity with an adapter.
- If the required interface change is too significant, an adapter might become overly complex and difficult to maintain.

## Trade-offs
### Pros
- **Single Responsibility Principle**: You can separate the interface or data conversion code from the primary business logic of the program.
- **Open/Closed Principle**: You can introduce new types of adapters into the program without breaking the existing client code, as long as they work with the client interface.
- **Reusability**: Allows the use of existing functionality even if the interfaces are incompatible.

### Cons
- **Complexity**: The overall complexity of the code increases because you need to introduce a set of new interfaces and classes. Sometimes it's simpler just to change the service class so that it matches the rest of your code.
