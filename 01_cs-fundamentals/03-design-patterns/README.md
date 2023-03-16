# Design Patterns in Practice

A comprehensive implementation of 12 classic Gang of Four (GoF) design patterns in **Python 3.10+** and **JavaScript (ES2022)**.

## Features
- **Creational Patterns**: Singleton, Factory, Builder.
- **Structural Patterns**: Adapter, Decorator, Facade, Proxy.
- **Behavioural Patterns**: Observer, Strategy, Command, Iterator, Template Method.
- **Refactoring Exercise**: A "before and after" case study of refactoring a God Class.

## Learning Objectives
- Recognize common software design problems and apply appropriate GoF patterns.
- Implement thread-safe, decoupled, and extensible architectures.
- Transition from "God Class" architectures to clean, modular designs via refactoring.
- Compare pattern implementations across different paradigms (Python vs. JavaScript).

## Project Structure
- `patterns/`: Implementation of patterns in Python and JavaScript.
- `refactoring/`: Refactoring exercise with `before` and `after` code.
- `tests/`: Pytest suite for Python implementations.

## Requirements
- Python 3.10+
- Node.js (for JS implementations)
- `pytest` and `pytest-asyncio` (for Python tests)

## How to Run
### Python
Run individual pattern real-world examples:
```bash
python patterns/behavioural/command/python/real_world.py
```

### JavaScript
Run individual pattern examples:
```bash
node patterns/behavioural/command/js/pattern.js
```

## Testing
Run the Python test suite:
```bash
pytest
```