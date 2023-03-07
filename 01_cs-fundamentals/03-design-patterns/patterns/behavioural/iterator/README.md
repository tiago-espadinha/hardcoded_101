# Iterator Pattern

## Problem it Solves
The Iterator pattern lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.). It abstracts the way you access each element so that the client doesn't need to know the structure of the collection.

## UML Description
- **Iterator**: Defines an interface for accessing and traversing elements.
- **Concrete Iterator**: Implements the Iterator interface and keeps track of the current position in the traversal.
- **Aggregate**: Defines an interface for creating an Iterator object.
- **Concrete Aggregate**: Implements the Iterator creation interface to return an instance of the proper Concrete Iterator.

## When to Use
- When your collection has a complex data structure under the hood, but you want to hide its complexity from clients.
- When you want to reduce duplication of traversal code across your app.
- When you want your code to be able to traverse different data structures or even structures whose types are unknown beforehand.

## When NOT to Use
- When your collection is a simple array/list and standard language iterators (like for-in) are sufficient.
- When traversal is highly specialized and not meant to be reused.

## Trade-offs
### Pros
- **Single Responsibility Principle**: You can clean up the client code and the collections by extracting bulky traversal algorithms into separate classes.
- **Open/Closed Principle**: You can implement new types of collections and iterators and pass them to existing code without breaking anything.
- **Parallel Traversal**: You can traverse the same collection in parallel because each iterator object contains its own iteration state.

### Cons
- **Overhead**: Applying the pattern might be an overkill if your app only works with simple collections.
- **Complexity**: It can be more complex to implement than simple loop traversal.
