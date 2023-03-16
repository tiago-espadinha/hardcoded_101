# Command Pattern

## Problem it Solves
The Command pattern turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request's execution, and support undoable operations.

## UML Description
- **Command**: Declares an interface for executing an operation.
- **Concrete Command**: Defines a binding between a Receiver object and an action. Implements `execute` by invoking the corresponding operation(s) on Receiver.
- **Client**: Creates a Concrete Command object and sets its receiver.
- **Invoker**: Asks the command to carry out the request.
- **Receiver**: Knows how to perform the operations associated with carrying out a request.

## When to Use
- When you want to parameterize objects by an action to perform.
- When you want to specify, queue, and execute requests at different times.
- When you need to support undo/redo functionality.
- When you want to decouple the object that invokes the operation from the one that knows how to perform it.

## When NOT to Use
- When the operation is simple and doesn't need to be encapsulated as an object.
- When you don't need to support undo, queuing, or other command features.
- When the overhead of creating command objects for every action is too high.

## Trade-offs
### Pros
- **Decoupling**: Decouples the invoker from the receiver.
- **Extensibility**: You can add new commands without changing existing code.
- **Complexity Management**: Allows for complex operations to be built from simple ones.
- **Undo/Redo**: Simplifies the implementation of undoable operations.

### Cons
- **Number of Classes**: Can lead to a large number of command classes.
- **Overhead**: Each command is an object, which can add memory and processing overhead.
