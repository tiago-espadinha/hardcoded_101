# Factory Method Pattern

## Problem It Solves
The Factory Method pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. It decouples the client code from the concrete classes it needs to instantiate.

## UML Description
- `Product`: Interface/ABC for the objects created (e.g., `DocumentParser`).
- `ConcreteProduct`: Specific implementations (e.g., `JSONParser`, `CSVParser`).
- `Creator`: The factory class/method that returns the products.

## When to use
- When a class can't anticipate the class of objects it must create.
- When you want to delegate the responsibility of object creation to a central place.
- When you want to provide users of your library with a way to extend its internal components.

## When NOT to use
- For simple object creation where the overhead of a factory is unnecessary.
- If you only have one type of product and it's unlikely to change.

## Trade-offs
- **Pros**: Avoids tight coupling between creator and concrete products, Single Responsibility Principle (creation code in one place), Open/Closed Principle (can add new products without breaking client code).
- **Cons**: Can make the code more complex by introducing multiple new classes and interfaces.
