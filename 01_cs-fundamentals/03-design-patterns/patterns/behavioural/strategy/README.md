# Strategy Pattern

## Problem it Solves
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it. It avoids having multiple conditional statements to choose an algorithm.

## UML Description
- **Strategy**: Defines an interface common to all supported algorithms. Context uses this interface to call the algorithm defined by a Concrete Strategy.
- **Concrete Strategy**: Implements the algorithm using the Strategy interface.
- **Context**: Is configured with a Concrete Strategy object and maintains a reference to a Strategy object.

## When to Use
- When many related classes differ only in their behavior.
- When you need different variants of an algorithm.
- When an algorithm uses data that clients shouldn't know about.
- When a class defines many behaviors, and these appear as multiple conditional statements in its operations.

## When NOT to Use
- When there are only a few strategies and they rarely change.
- When clients must be aware of how strategies differ to select the right one.
- When the overhead of creating strategy objects and passing them to the context is not justified.

## Trade-offs
### Pros
- **Clean Code**: Replaces complex conditionals with a clean interface.
- **Open/Closed Principle**: You can introduce new strategies without changing the context.
- **Isolation**: Each algorithm is isolated in its own class, making it easier to test and maintain.

### Cons
- **Increased Number of Objects**: Each strategy is a separate class/object.
- **Client Knowledge**: Clients must know about the different strategies to choose the appropriate one.
