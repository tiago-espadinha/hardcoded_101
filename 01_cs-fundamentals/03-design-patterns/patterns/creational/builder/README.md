# Builder Pattern

## Problem It Solves
The Builder pattern is used to construct complex objects step by step. It allows you to produce different types and representations of an object using the same construction code. It's particularly useful when an object has many optional parameters or a complex initialization process.

## UML Description
- `Builder`: Interface or base class for creating parts of a `Product` object.
- `ConcreteBuilder`: Implements the `Builder` interface and tracks the representation it creates.
- `Director`: (Optional) Constructs an object using the `Builder` interface.
- `Product`: The complex object being built.

## When to use
- When you want to get rid of a "telescoping constructor" (a constructor with too many parameters).
- When you want your code to be able to create different representations of some product (e.g. JSON, XML, HTML exporters).
- When construction steps must be performed in a specific order.

## When NOT to use
- If the object being built is simple and doesn't require many steps or optional parameters.
- If the product's construction is already straightforward.

## Trade-offs
- **Pros**: Can construct objects step-by-step, defer construction steps, or run steps recursively. Single Responsibility Principle (isolates complex construction code from business logic).
- **Cons**: Increases overall complexity by adding multiple new classes.
