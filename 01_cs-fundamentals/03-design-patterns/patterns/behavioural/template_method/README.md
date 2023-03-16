# Template Method Pattern

## Problem it Solves
The Template Method pattern defines the skeleton of an algorithm in a base class but lets subclasses override specific steps of the algorithm without changing its structure. It helps to avoid code duplication by moving common behavior to a base class.

## UML Description
- **Abstract Class**: Defines abstract primitive operations that concrete subclasses implement to carry out steps of an algorithm. It also implements a template method defining the skeleton of an algorithm.
- **Concrete Class**: Implements the primitive operations to carry out subclass-specific steps of the algorithm.

## When to Use
- When you want to let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.
- When you have several classes that contain almost identical algorithms with some minor differences.
- When you want to implement the "Holleywood Principle" (Don't call us, we'll call you), where the base class calls the methods of subclasses.

## When NOT to Use
- When the algorithm is simple and doesn't have many common steps across different variants.
- When you need to change the overall structure of the algorithm in subclasses.
- When the number of steps that need to be overridden is too large, making the pattern hard to manage.

## Trade-offs
### Pros
- **Code Reuse**: Moves common code to a base class.
- **Extensibility**: Lets subclasses override only certain parts of a large algorithm.
- **Control**: The base class controls the algorithm's execution flow.

### Cons
- **Rigidity**: Some clients may be limited by the skeleton algorithm.
- **Inheritance Complexity**: Violates the Liskov Substitution Principle if not used carefully.
- **Maintenance**: Maintaining the template method can become difficult if it has too many steps.
