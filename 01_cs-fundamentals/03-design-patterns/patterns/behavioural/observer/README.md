# Observer Pattern

## Problem it Solves
The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. It's the foundation for event-driven systems.

## UML Description
- **Subject**: Knows its observers and provides an interface for attaching/detaching Observer objects.
- **Observer**: Defines an updating interface for objects that should be notified of changes in a subject.
- **Concrete Subject**: Stores state of interest to Concrete Observer objects and sends a notification to its observers when its state changes.
- **Concrete Observer**: Maintains a reference to a Concrete Subject and implements the Observer updating interface.

## When to Use
- When an abstraction has two aspects, one dependent on the other.
- When a change to one object requires changing others, and you don't know how many objects need to be changed.
- When an object should be able to notify other objects without making assumptions about who these objects are.

## When NOT to Use
- When the relationship between subjects and observers is very complex and creates circular dependencies.
- When notifications are not needed (the "push" model is overhead if polling is more efficient).
- When the order of notification is critical, as Observer doesn't typically guarantee it.

## Trade-offs
### Pros
- **Loose Coupling**: Subjects and observers are loosely coupled; the subject doesn't need to know the concrete class of the observer.
- **Open/Closed Principle**: You can introduce new subscriber classes without having to change the publisher's code.

### Cons
- **Memory Leaks**: If observers are not properly detached, they might prevent the subject from being garbage collected.
- **Complexity**: It can be difficult to track the flow of events in a large system with many observers.
