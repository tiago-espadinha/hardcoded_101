# Luma Language (luma-lang)

A tree-walking interpreter for the Luma programming language, implemented in Python 3.10+.

## Features
- **Core Types**: Integers, Floats, Strings, Booleans, and Null.
- **Control Flow**: `if/else`, `while` loops, `break`, `continue`.
- **Functions**: Lexical scoping, closures, and recursion.
- **Data Structures**: Arrays with indexing, `.push()`, and `.length`.
- **Lexer & Parser**: Hand-written recursive descent parser.

## Learning Objectives
- Understand the full lifecycle of a programming language (Source -> Tokens -> AST -> Execution).
- Implement a hand-written recursive descent parser and lexical analyzer.
- Manage execution state, lexical scoping, and closures using environment stacks.
- Build a functional REPL and tree-walking evaluator.

## Project Structure
- `lexer.py`: Tokenizes source code into discrete tokens.
- `parser.py`: Parses tokens into an Abstract Syntax Tree (AST).
- `ast_nodes.py`: Defines the AST nodes.
- `environment.py`: Manages variable scoping and storage.
- `interpreter.py`: Evaluates the AST to execute the program.
- `luma.py`: Entry point for running scripts and the REPL.
- `examples/`: Example Luma programs (`fizzbuzz.luma`, etc.).
- `tests/`: Comprehensive test suite for the language.

## Requirements
- Python 3.10+
- `pytest` (for running tests)

## How to Run
To run a Luma script:
```bash
python luma.py examples/fizzbuzz.luma
```
To enter the interactive REPL:
```bash
python luma.py
```

## Testing
Run the test suite using pytest:
```bash
pytest
```