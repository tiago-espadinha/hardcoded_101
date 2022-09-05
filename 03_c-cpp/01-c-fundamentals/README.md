# C Fundamentals: Memory, Pointers, and Systems Programming

A hands-on C project exploring how memory really works — stacks, heaps, and pointers — through progressively complex exercises. Understanding these mechanics makes you a materially better programmer in every language you use afterwards.

## Features

- **Memory & Pointers Module**: Pointer arithmetic, stack vs heap allocation, array–pointer equivalence, custom string functions, and struct manipulation — all with AddressSanitizer verification.
- **Data Structures in C**: Singly linked list and open-addressing hash table implemented from scratch with proper allocation and NULL safety throughout.
- **File I/O Module**: A CSV-backed command-line grade tracker and a binary file I/O benchmark comparing text vs binary representation for large integer arrays.
- **Sanitizer-First Development**: Every module compiles with `-fsanitize=address,undefined` to catch undefined behaviour, leaks, and out-of-bounds access at development time.

## Learning Objectives

- Read and write pointer declarations and arithmetic confidently.
- Manage heap memory without leaks, verified with ASan/Valgrind.
- Understand why C is fast and why it is dangerous.
- Build and use a Makefile with separate debug and release targets.

## Project Structure

```
c-fundamentals/
├── Makefile
├── README.md
├── memory/
│   ├── 01_pointers.c          — pointer basics, address printing, arithmetic
│   ├── 02_stack_vs_heap.c     — malloc/free, dangling pointers, leak demo
│   ├── 03_pointers_and_arrays.c — arr[i] == *(arr+i), 2D heap arrays
│   ├── 04_strings.c           — my_strlen/strcpy/strcat/strcmp/strrev
│   └── 05_structs.c           — Student struct, pass-by-value vs pointer, sort
├── structures/
│   ├── linked_list.h          — singly linked list interface
│   ├── linked_list.c          — full linked list implementation
│   ├── hash_table.h           — open-addressing hash table interface
│   └── hash_table.c           — djb2 hash, linear probing, auto-resize
└── files/
    ├── grade_tracker.c        — CSV grade tracker CLI
    └── binary_rw.c            — binary file write/read/benchmark
```

## Requirements

- GCC 9+ or Clang 10+ with C17 support
- GNU Make
- (Optional) Valgrind for additional memory checking on Linux

## How to Run

Build and run all memory exercises:

```bash
make debug
./memory/01_pointers
./memory/02_stack_vs_heap
./memory/03_pointers_and_arrays
./memory/04_strings
./memory/05_structs
```

Run the data structures demos:

```bash
./structures/linked_list
./structures/hash_table
```

Use the grade tracker:

```bash
./files/grade_tracker add "Alice" 88 92 95
./files/grade_tracker list
./files/grade_tracker average 1
./files/grade_tracker top 3
```

Run the binary I/O benchmark:

```bash
./files/binary_rw
```

## Build Targets

| Target | Description |
|--------|-------------|
| `make debug` | Compile all with `-g -fsanitize=address,undefined` |
| `make release` | Compile all with `-O2` |
| `make test` | Run automated shell test suite |
| `make clean` | Remove all compiled binaries and object files |

## Testing

```bash
make test
```

The test script exercises every module and reports pass/fail for each section.
