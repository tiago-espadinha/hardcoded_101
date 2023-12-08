# Module Name: C++ Mastery: OOP & STL

A comprehensive guide to transitioning from C to idiomatic modern C++ (C++17), focusing on RAII, ownership semantics, and the STL.

## Features
- **OOP Fundamentals**: Deep dive into classes, RAII, inheritance, and templates.
- **Modern C++**: Mastering smart pointers, STL algorithms, move semantics, and lambdas.
- **Data Structures**: Re-implementing hash maps and doubly linked lists in modern C++.
- **Automated Testing**: Comprehensive testing with Catch2.

## Learning Objectives
- Implement complex logic without relying on third-party magic.
- Understand the underlying mechanics of RAII and move semantics.
- Analyze performance characteristics using real-world benchmarks.

## Project Structure
- `oop/`: Fundamental OOP concepts (RAII, Inheritance, Templates).
- `modern/`: Modern C++ features (Smart pointers, STL algorithms, Lambdas).
- `cpp_hash_map/`: Custom template hash map implementation.
- `cpp_linked_list/`: Custom template doubly linked list implementation.
- `tests/`: Comprehensive test suite using Catch2.

## Requirements
- CMake 3.10+
- C++17 compliant compiler (GCC 7+, Clang 5+, MSVC 19.14+)

## How to Run
```bash
mkdir build && cd build
cmake ..
make
```

## Testing
Run all tests using CTest:
```bash
ctest
```
