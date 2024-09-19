# Module Name: chatd - TCP Socket Server in C

A multi-client TCP chat server implementation using POSIX sockets and pthreads, featuring a thread pool and room management.

## Features
- **Multi-threaded Server**: Uses a custom thread pool to handle up to 100 simultaneous connections efficiently.
- **Room Management**: Supports multiple chat rooms with a default "general" room and private messaging.
- **Graceful Shutdown**: Handles SIGINT and SIGTERM to ensure all resources are freed and connections closed cleanly.
- **Interactive Client**: A multi-threaded client for real-time communication.

## Learning Objectives
- Implement complex logic without relying on third-party magic.
- Understand the underlying mechanics of TCP connections, sockets, and multi-threaded synchronization.
- Analyze performance characteristics using real-world load testing.

## Project Structure
- `server.c`, `server.h`: Core server logic and socket handling.
- `thread_pool.c`, `thread_pool.h`: Custom thread pool implementation.
- `rooms.c`, `rooms.h`: Chat room and user management logic.
- `client.c`: Multi-threaded client implementation.
- `tests/`: Load tests and protocol verification scripts.

## Requirements
- GCC (C17 support)
- POSIX-compliant system (Linux recommended)
- Python 3 for running tests

## How to Run
Compile the server and client using the provided Makefile:
```bash
make
./chatd
./client localhost 8080
```

## Testing
Run the protocol tests:
```bash
python3 tests/test_protocol.py
```
Or the load tests:
```bash
python3 tests/load_test.py
```
